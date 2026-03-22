import json
import random
import os

def generate_video_metadata(output_file="input_tags.json", duration=7200, num_events=8, tags_per_event=120):
    """
    Generates synthetic user engagement data for video highlight analysis.
    
    :param output_file: Path to save the generated JSON data.
    :param duration: Total video length in seconds (default 2 hours).
    :param num_events: Number of 'High Interest' anchors (e.g., goals, bosses, kills).
    :param tags_per_event: Number of user tags generated around each anchor.
    """
    
    print(f"--- Starting Data Simulation ---")
    print(f"Target Duration: {duration}s")
    
    all_tags = []
    
    # 1. Generate 'Event Anchors' (Hidden Ground Truth)
    # These represent the actual highlights the algorithm should find.
    anchors = [random.randint(300, duration - 300) for _ in range(num_events)]
    anchors.sort()
    
    print(f"Simulating {num_events} high-intensity events at: {anchors}")

    for anchor in anchors:
        for _ in range(tags_per_event):
            # Simulate human reaction latency (users tag slightly after the event)
            # and varying attention spans (length of the highlight tag).
            start_offset = random.randint(-5, 15) 
            length = random.randint(10, 45)
            
            start = max(0, anchor + start_offset)
            end = min(duration, start + length)
            
            # Engagement intensity (weighted 1 to 10)
            intensity = random.randint(1, 10)
            
            all_tags.append({
                "start": start,
                "end": end,
                "intensity": intensity
            })

    # 2. Add Background Noise (Random low-intensity chatter)
    noise_count = num_events * 25
    for _ in range(noise_count):
        start = random.randint(0, duration - 60)
        end = start + random.randint(5, 25)
        all_tags.append({
            "start": start,
            "end": end,
            "intensity": random.randint(1, 3)
        })

    # Shuffle the list to simulate unsorted real-world log ingestion
    random.shuffle(all_tags)

    # 3. Export to JSON
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(all_tags, f, indent=4)
        
        file_size = os.path.getsize(output_file) / 1024 # KB
        print(f"Successfully generated {len(all_tags)} tags.")
        print(f"Output saved to: {output_file} ({file_size:.2f} KB)")
        print(f"--- Simulation Complete ---")
        
    except Exception as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    # You can change these parameters to test the Segment Tree's scale limits
    generate_video_metadata(
        output_file="input_tags.json", 
        duration=7200, 
        num_events=10, 
        tags_per_event=150
    )