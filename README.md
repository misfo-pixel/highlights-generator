# Smart Video Highlights Generator

A high-performance tool for detecting video high-intensity segments using a **Segment Tree** (OCaml) and a **Greedy Selection** strategy (Python).

## 1. Overview
This project processes "interest tags" from long-form videos to automatically extract the most engaging clips within a specified time limit. It bridges the gap between raw interval data and professional-grade highlight reels.

## 2. Prerequisites
- **OCaml 4.14+**: For the core recursive logic.
- **Python 3.10+**: For data simulation and greedy optimization.

## 3. Installation & Setup
Clone the repository and ensure your OCaml environment is active:
```bash
git clone [https://github.com/misfo_pixel/highlights-generator](https://github.com/misfo_pixel/highlights-generator)
cd highlights-generator
python simulator.py
```

## 4. Reference

### generate_video_metadata()

Generates synthetic user engagement data for video highlight analysis.

- param output_file: Path to save the generated JSON data.
- param duration: Total video length in seconds (default 2 hours).
- param num_events: Number of 'High Interest' anchors (e.g., goals, bosses, kills).
- param tags_per_event: Number of user tags generated around each anchor.