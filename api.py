import aiohttp
import asyncio
import pandas as pd
import sys
import time

API_KEY = "579b464db66ec23bdd0000010cebaf31b6854cb77de768e7e2d13018"

async def fetch_data_async(url, topic, retries=3, backoff_factor=2):
    print(f"🚀 Initiating {topic} data fetch from data.gov.in...")
    progress = 0
    bar_length = 50
    start_time = time.time()

    async def update_progress():
        nonlocal progress
        while progress < 90:
            filled = int(bar_length * progress // 100)
            bar = '=' * filled + ' ' * (bar_length - filled)
            elapsed_time = time.time() - start_time + 0.1
            simulated_speed = (progress * 10) / elapsed_time
            sys.stdout.write(f"\r[{bar}] {progress}%  Speed: {simulated_speed:.1f} KB/s")
            sys.stdout.flush()
            await asyncio.sleep(0.2)
            progress += 10
        filled = int(bar_length * progress // 100)
        bar = '=' * filled + ' ' * (bar_length - filled)
        elapsed_time = time.time() - start_time + 0.1
        simulated_speed = (progress * 10) / elapsed_time
        sys.stdout.write(f"\r[{bar}] {progress}%  Speed: {simulated_speed:.1f} KB/s")
        sys.stdout.flush()

    for attempt in range(retries):
        progress_task = asyncio.create_task(update_progress())
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    await progress_task
                    if response.status == 200:
                        progress = 100
                        filled = bar_length
                        bar = '=' * filled
                        elapsed_time = time.time() - start_time + 0.1
                        simulated_speed = (progress * 10) / elapsed_time
                        sys.stdout.write(f"\r[{bar}] {progress}%  Speed: {simulated_speed:.1f} KB/s")
                        sys.stdout.flush()
                        print()
                        data = await response.json()
                        return pd.DataFrame(data['records'])
                    else:
                        raise Exception(f"Failed to fetch {topic} data: HTTP {response.status}")
        except Exception as e:
            progress_task.cancel()
            sys.stdout.write("\r" + " " * 70 + "\r")
            sys.stdout.flush()
            if attempt < retries - 1:
                wait_time = backoff_factor ** attempt
                print(f"❌ Attempt {attempt + 1} failed: {str(e)}. Retrying in {wait_time} seconds...")
                await asyncio.sleep(wait_time)
            else:
                print(f"❌ Failed to fetch {topic} data after {retries} attempts: {str(e)}")
                raise e

async def fetch_plastic_waste_data():
    url = f"https://api.data.gov.in/resource/ad39c33f-9d07-41a8-9a7d-06081e01617f?api-key={API_KEY}&format=json&limit=100"
    return await fetch_data_async(url, "Plastic Waste")

async def fetch_wastewater_data():
    url = f"https://api.data.gov.in/resource/e374f644-b9d4-4e2a-b55f-f3888859abd6?api-key={API_KEY}&format=json&limit=100"
    return await fetch_data_async(url, "Wastewater")