#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
"""
STEMAIDE Docs - HTML to Markdown Reconstruction Script
Extracts content from built HTML files and creates proper .md source files
"""

import os
import re
from pathlib import Path
import html2text

DOCS_DIR = Path("docs")

def get_article_html(html_file):
    """Extract article content from a MkDocs-built HTML file."""
    if not html_file.exists():
        return None
    try:
        with open(html_file, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        match = re.search(r'(?s)<article[^>]*>(.*?)</article>', content)
        if match:
            return match.group(1).strip()
    except Exception as e:
        print(f"  ERROR reading {html_file}: {e}")
    return None


def html_to_markdown(html_content):
    """Convert HTML content to clean Markdown."""
    if not html_content:
        return ""
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.body_width = 0
    h.unicode_snob = True
    h.skip_internal_links = False
    h.protect_links = False
    h.ignore_anchors = True
    md = h.handle(html_content)
    # Remove MkDocs anchor/permalink symbols
    md = re.sub(r'\s*\[¶\]\([^)]*\)', '', md)
    md = re.sub(r'\[\\¶\]\([^)]*\)', '', md)
    md = re.sub(r'\[&para;\]\([^)]*\)', '', md)
    # Clean up nav tags remnant
    md = re.sub(r'(?s)<nav[^>]*>.*?</nav>', '', md)
    # Remove excess blank lines (max 2 consecutive)
    md = re.sub(r'\n{3,}', '\n\n', md)
    return md.strip()


def md_path_to_html_path(md_rel_path):
    """Convert a relative .md nav path to its built HTML file path."""
    p = Path(md_rel_path)
    if p.name == 'index.md':
        # Section index: path/to/section/index.md -> docs/path/to/section/index.html
        return DOCS_DIR / p.parent / 'index.html'
    else:
        # Leaf page: path/to/page.md -> docs/path/to/page/index.html
        return DOCS_DIR / p.parent / p.stem / 'index.html'


def write_md_file(md_rel_path, content):
    """Write markdown content to file in docs/."""
    output_path = DOCS_DIR / md_rel_path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content.strip() + '\n')
    print(f"  [OK] {md_rel_path}")


def process_entry(md_rel_path, fallback_title=None):
    """Process a single nav entry: extract HTML content -> write .md file."""
    html_path = md_path_to_html_path(md_rel_path)
    html_content = get_article_html(html_path)

    if html_content:
        md_content = html_to_markdown(html_content)
        if md_content:
            write_md_file(md_rel_path, md_content)
            return True

    # Fallback: create stub
    title = fallback_title or Path(md_rel_path).stem.replace('-', ' ').replace('_', ' ').title()
    write_md_file(md_rel_path, f"# {title}\n\nContent coming soon.\n")
    print(f"    [stub] HTML not found at: {html_path}")
    return False


# ---------------------------------------------
# All entries to reconstruct
# ─────────────────────────────────────────────
NAV_ENTRIES = [
    # Root & global pages
    ("index.md", "Home"),
    ("about.md", "About STEMAIDE"),
    ("CHANGELOG.md", "Changelog"),
    ("CONTRIBUTING.md", "Contributing"),
    ("code-of-conduct.md", "Code of Conduct"),

    # Getting Started
    ("getting-started/overview.md", "Overview"),
    ("getting-started/installation.md", "Installation"),
    ("getting-started/quick-start.md", "Quick Start"),

    # Features
    ("features/core-features.md", "Core Features"),
    ("features/advanced-features.md", "Advanced Features"),

    # Guides
    ("guides/user-guide.md", "User Guide"),
    ("guides/developer-guide.md", "Developer Guide"),

    # Use Cases landing
    ("use-case/index.md", "Use Cases"),

    # ── Beginner (1.0) ──
    ("1.0/index.md", "Beginner Use Cases"),

    # LED
    ("1.0/1.1.LED/index.md", "LED Control"),
    ("1.0/1.1.LED/1.1.1.LED_ON.md", "LED ON"),
    ("1.0/1.1.LED/1.1.2.One_LED_Blink.md", "CAR TRAVIGATOR BLINKING"),
    ("1.0/1.1.LED/1.1.3.LEDS_ON.md", "DOUBLE LED ON"),
    ("1.0/1.1.LED/1.1.4.Two_LED_Blink.md", "DOUBLE LED BLINK"),
    ("1.0/1.1.LED/1.1.5.Three_LEDs_ON.md", "Triple LEDS"),
    ("1.0/1.1.LED/1.1.6.Three_LEDs_Blink.md", "TRAFFIC LIGHT"),
    ("1.0/1.1.LED/1.1.7.Four_LEDs_ON.md", "Car Front and Rear Lights"),
    ("1.0/1.1.LED/1.1.8.Four_LEDs_Blink.md", "PARTY LIGHTS"),
    ("1.0/1.1.LED/1.1.9.Five_LEDs_ON.md", "INCREASING BRIGHTNESS IN A ROOM"),
    ("1.0/1.1.LED/1.1.10.Five_LEDs_Blink.md", "PARTY LIGHTENING"),

    # Buzzer
    ("1.0/1.2.Buzzer/index.md", "Buzzer Control"),
    ("1.0/1.2.Buzzer/1.2.1.Buzzer_ON_and_OFF.md", "Buzzer ON and OFF"),
    ("1.0/1.2.Buzzer/1.2.2.Buzzer_Beep.md", "Buzzer Beep"),

    # Push Button
    ("1.0/1.3.Push_Button/index.md", "Push Button Interface"),
    ("1.0/1.3.Push_Button/1.3.1.Push_Button_press_with_1_LED.md", "BUTTON LIT"),
    ("1.0/1.3.Push_Button/1.3.2.Push_Button_press_with_2_LEDs.md", "TWIN LIGHT"),
    ("1.0/1.3.Push_Button/1.3.3.Push_Button_press_with_3_LEDs.md", "TRI-LIGHT"),

    # Traffic Light
    ("1.0/1.4.Traffic_Light/index.md", "Traffic Light Module"),
    ("1.0/1.4.Traffic_Light/1.4.0.Taffic_Light_Intro.md", "TRAFFIC LIGHT Intro"),
    ("1.0/1.4.Traffic_Light/1.4.1.Traffic_Light_Red_ON.md", "RED MEANS STOP"),
    ("1.0/1.4.Traffic_Light/1.4.2.Traffic_Light_Red_BLINK.md", "TRAFFIC LIGHT RED BLINK"),
    ("1.0/1.4.Traffic_Light/1.4.3.Traffic_Light_Yellow_ON.md", "YELLOW MEANS GET READY"),
    ("1.0/1.4.Traffic_Light/1.4.4.Traffic_Light_Yellow_Blink.md", "TRAFFIC LIGHT YELLOW BLINK"),
    ("1.0/1.4.Traffic_Light/1.4.5.Traffic_Light_Green_ON.md", "Green Means Go"),
    ("1.0/1.4.Traffic_Light/1.4.6.Traffic_Light_Green_Blink.md", "Traffic Light Green Blink"),

    # RGB
    ("1.0/1.5.RGB/index.md", "RGB LED Module"),
    ("1.0/1.5.RGB/1.5.1.RGB_Red_On.md", "RGB Red On"),
    ("1.0/1.5.RGB/1.5.2.RGB_Red_Blink.md", "Red Blink"),
    ("1.0/1.5.RGB/1.5.3.RGB_Green_On.md", "Turning On Green LED on RGB"),
    ("1.0/1.5.RGB/1.5.4.RGB_Green_Blink.md", "Green LED Blinking on RGB"),
    ("1.0/1.5.RGB/1.5.5.RGB_Blue_On.md", "RGB Blue On"),
    ("1.0/1.5.RGB/1.5.6.RGB_Blue_Blink.md", "Blue LED Blinking on RGB"),
    ("1.0/1.5.RGB/1.5.7.RGB_Rainbow_Colors.md", "Rainbow Colors on RGB"),

    # LDR
    ("1.0/1.6.LDR/index.md", "LDR Light Sensor"),
    ("1.0/1.6.LDR/1.6.0.LDR_Module.md", "LIGHT INTENSITY CHECKER"),

    # Servo
    ("1.0/1.7.Servo_Motor/index.md", "Servo Motor Control"),
    ("1.0/1.7.Servo_Motor/1.7.0.Servo_Motor_One_Angle.md", "ROBOT ARM-UP"),
    ("1.0/1.7.Servo_Motor/1.7.1.Servo_Motor_Sweep.md", "Car Windshield Wiper"),

    # Sound Sensor
    ("1.0/1.9.Sound_Sensor/index.md", "Sound Sensor Interface"),
    ("1.0/1.9.Sound_Sensor/1.9.0.Sound_Sensor.md", "Noise Checker"),

    # ── Intermediate (2.0) ──
    ("2.0/index.md", "Intermediate Use Cases"),

    # Ultrasonic + LED
    ("2.0/2.1.Ultrasonic+LED/index.md", "Ultrasonic Sensor and LED"),
    ("2.0/2.1.Ultrasonic+LED/2.1.1.Ultrasonic_and_1_LED.md", "Ultrasonic with 1 LED"),
    ("2.0/2.1.Ultrasonic+LED/2.1.2.Ultrasonic_and_2_LED.md", "Ultrasonic with 2 LEDs"),
    ("2.0/2.1.Ultrasonic+LED/2.1.3.Ultrasonic_and_3_LED.md", "Ultrasonic with 3 LEDs"),
    ("2.0/2.1.Ultrasonic+LED/2.1.4.Ultrasonic_and_4_LED.md", "SMART ALERT LIGHTING SYSTEM"),

    # Ultrasonic + Buzzer
    ("2.0/2.2.Ultrasonic+Buzzer/index.md", "Ultrasonic and Buzzer"),
    ("2.0/2.2.Ultrasonic+Buzzer/2.2.1.Ultrasonic_distance_Sensor.md", "SMART SOUND ALERT SYSTEM"),

    # Ultrasonic + Traffic Light
    ("2.0/2.3.Ultrasonic+TrafficLight/index.md", "Ultrasonic and Traffic Light"),
    ("2.0/2.3.Ultrasonic+TrafficLight/2.3.1.ultrasonic_sensor_and_trafficLight_module.md", "Ultrasonic with Traffic Light Module"),

    # Ultrasonic + RGB
    ("2.0/2.4.Ultrasonic+RGB/index.md", "Ultrasonic and RGB Module"),
    ("2.0/2.4.Ultrasonic+RGB/2.4.1.ultrasonic_sensor_and_RGB_module.md", "Smart Lighting System with RGB"),

    # Push Button + LED
    ("2.0/2.5.Push_Button+LED/index.md", "Push Button and LED"),
    ("2.0/2.5.Push_Button+LED/2.5.1.Push_Button_to_turn_on_and_off_LED.md", "Control LED with Push Button"),
    ("2.0/2.5.Push_Button+LED/2.5.2.Push_Button_to_blink_one_LED.md", "Blink LED with Push Button"),
    ("2.0/2.5.Push_Button+LED/2.5.3.Push_Button_to_turn_on_and_off_2_LED.md", "Control 2 LEDs with Push Button"),
    ("2.0/2.5.Push_Button+LED/2.5.4.Push_Button_to_blink_two_LED.md", "Blink 2 LEDs with Push Button"),
    ("2.0/2.5.Push_Button+LED/2.5.5.Push_Button_to_turn_on_and_off_three_LED.md", "Control 3 LEDs with Push Button"),
    ("2.0/2.5.Push_Button+LED/2.5.7.Push_Button_to_turn_on_and_off_four_LED.md", "Control 4 LEDs with Push Button"),
    ("2.0/2.5.Push_Button+LED/2.5.8.Push_Button_to_blink_four_LED.md", "Blink 4 LEDs with Push Button"),

    # Push Button + Buzzer
    ("2.0/2.6.Push_Button+Buzzer/index.md", "Push Button and Buzzer"),
    ("2.0/2.6.Push_Button+Buzzer/2.6.1.Push_button_and_Buzzer.md", "Push Button with Buzzer"),

    # Push Button + Traffic Light
    ("2.0/2.7.PushButton+TrafficLightModule/index.md", "Push Button and Traffic Light"),
    ("2.0/2.7.PushButton+TrafficLightModule/2.7.1.PushButton+TrafficLightModule.md", "Push Button with Traffic Light Module"),

    # Push Button + RGB
    ("2.0/2.8.PushButton+RGB/index.md", "Push Button and RGB"),
    ("2.0/2.8.PushButton+RGB/2.8.1.PushButton+RGB.md", "Pushbutton And RGB Control"),

    # LDR + LED
    ("2.0/2.9.LDR+LED/index.md", "LDR Sensor and LED"),
    ("2.0/2.9.LDR+LED/2.9.1.LDR+1_LED.md", "Smart Street Light (1 LED)"),
    ("2.0/2.9.LDR+LED/2.9.2.LDR+2_LED.md", "Smart Street Light (2 LEDs)"),
    ("2.0/2.9.LDR+LED/2.9.4.LDR+4_LED.md", "Smart Street Light (4 LEDs)"),
    ("2.0/2.9.LDR+LED/2.9.5.LDR+5_LED.md", "Smart Street Light (5 LEDs)"),

    # LDR + Buzzer
    ("2.0/2.10.LDR+Buzzer/index.md", "LDR Sensor and Buzzer"),
    ("2.0/2.10.LDR+Buzzer/2.10.1.LDR+Buzzer.md", "Smart Sound Alert System"),

    # LDR + RGB
    ("2.0/2.11.LDR_RGB/index.md", "LDR Sensor and RGB"),
    ("2.0/2.11.LDR_RGB/2.11.1.LDR_RGB.md", "LDR with RGB Module"),

    # STEMAIDE Traffic Light
    ("2.0/2.12.Traffic_Light_STEMAIDE/index.md", "STEMAIDE Traffic Light"),
    ("2.0/2.12.Traffic_Light_STEMAIDE/2.12.1.Traffic_Light_STEMAIDE.md", "Traffic Light with STEMAIDE"),

    # Sound Sensor + LED
    ("2.0/2.13.SoundSensor+LED/index.md", "Sound Sensor and LED"),
    ("2.0/2.13.SoundSensor+LED/2.13.1.SoundSensor+1_LED.md", "Sound Sensor with 1 LED"),
    ("2.0/2.13.SoundSensor+LED/2.13.2.Soundsensor+2_LED.md", "Sound Sensor with 2 LEDs"),
    ("2.0/2.13.SoundSensor+LED/2.13.3.SoundSensor+3_LED.md", "Sound Sensor with 3 LEDs"),

    # Sound Sensor + Traffic
    ("2.0/2.14.SoundSensor+Traffic/index.md", "Sound Sensor and Traffic Light"),
    ("2.0/2.14.SoundSensor+Traffic/2.14.1.SoundSensor+TrafficLight_module.md", "Sound Sensor with Traffic Light"),

    # ── Advanced (3.0) ──
    ("3.0/index.md", "Advanced Use Cases"),
    ("3.0/3.1.Smart_Guage/index.md", "Smart Gauge System"),
    ("3.0/3.1.Smart_Guage/3.1.1.Smart_Guage.md", "Smart Gauge Project"),
    ("3.0/3.2.Smart_Security_System/index.md", "Smart Security System"),
    ("3.0/3.2.Smart_Security_System/3.2.1.Smart_Security_System.md", "Smart Security System Project"),
    ("3.0/3.3.Smart_Traffic_light_system/index.md", "Smart Traffic Light System"),
    ("3.0/3.3.Smart_Traffic_light_system/3.3.1.Smart_Traffic_light_system.md", "Smart Traffic Light Project"),
    ("3.0/3.4.Smart_Bed_Light/index.md", "Smart Bed Light System"),
    ("3.0/3.4.Smart_Bed_Light/3.4.1.Smart_Bed_Light.md", "Smart Bed Light Project"),
    ("3.0/3.5.Smart_Car_Parking_System/index.md", "Smart Car Parking System"),
    ("3.0/3.5.Smart_Car_Parking_System/3.5.1.Smart_Car_Parking_System.md", "Smart Car Parking Project"),
    ("3.0/3.6.Smart_Clap_Device/index.md", "Smart Clap Device"),
    ("3.0/3.6.Smart_Clap_Device/3.6.1.Smart_Clap_device.md", "Smart Clap Device Project"),
]

# Advanced section: original HTML folder names have spaces
ADVANCED_HTML_OVERRIDES = {
    "3.0/3.1.Smart_Guage/3.1.1.Smart_Guage.md":
        DOCS_DIR / "3.0/3.1.Smart_Guage/3.1.1.Smart Guage/index.html",
    "3.0/3.2.Smart_Security_System/3.2.1.Smart_Security_System.md":
        DOCS_DIR / "3.0/3.2.Smart_Security_System/3.2.1.Smart Security System/index.html",
    "3.0/3.3.Smart_Traffic_light_system/3.3.1.Smart_Traffic_light_system.md":
        DOCS_DIR / "3.0/3.3.Smart_Traffic_light_system/3.3.1.Smart Traffic light system/index.html",
}


# ─────────────────────────────────────────────
# Manual content for new section landing pages
# ─────────────────────────────────────────────
NEW_PAGES = {
    "getting-started/index.md": """\
# Getting Started

Welcome to the **STEMAIDE Kit** documentation! This section will help you set up your
environment and get your first project running in minutes.

## What You'll Find Here

- **Overview** — Introduction to the Arduino IDE and basic setup steps
- **Installation** — How to download and install the Arduino IDE
- **Quick Start** — Your first STEMAIDE project, step by step

---

Ready to begin? Start with the [Overview](overview.md).
""",
    "features/index.md": """\
# Features

Explore what the STEMAIDE Kit can do. This section covers both the core features
available out-of-the-box and the advanced capabilities for experienced builders.

## Sections

- [Core Features](core-features.md) — Fundamental components and capabilities
- [Advanced Features](advanced-features.md) — Extended functionality for complex projects
""",
    "guides/index.md": """\
# Guides

Detailed reference guides for working with the STEMAIDE Kit.

## Available Guides

- [User Guide](user-guide.md) — End-to-end usage instructions for learners
- [Developer Guide](developer-guide.md) — Technical reference for educators and contributors
""",
}


def main():
    print("=" * 60)
    print("STEMAIDE Docs — Markdown Reconstruction")
    print("=" * 60)

    # Write new manually-created section index pages
    print("\n[1/3] Creating new section landing pages...")
    for rel_path, content in NEW_PAGES.items():
        write_md_file(rel_path, content)

    # Extract content from HTML and write .md files
    print("\n[2/3] Extracting content from HTML files...")
    ok_count = 0
    stub_count = 0
    for md_rel_path, fallback_title in NAV_ENTRIES:
        # Check for override (advanced pages with spaces in filenames)
        if md_rel_path in ADVANCED_HTML_OVERRIDES:
            html_path = ADVANCED_HTML_OVERRIDES[md_rel_path]
            html_content = get_article_html(html_path)
            if html_content:
                md_content = html_to_markdown(html_content)
                if md_content:
                    write_md_file(md_rel_path, md_content)
                    ok_count += 1
                    continue
            write_md_file(md_rel_path, f"# {fallback_title}\n\nContent coming soon.\n")
            print(f"    [stub] HTML override not found: {html_path}")
            stub_count += 1
            continue

        result = process_entry(md_rel_path, fallback_title)
        if result:
            ok_count += 1
        else:
            stub_count += 1

    print(f"\n  Extracted: {ok_count} pages")
    print(f"  Stubs:     {stub_count} pages")

    print("\n[3/3] Done!")
    print("\nAll markdown source files have been written to docs/")
    print("Next steps:")
    print("  1. Run: mkdocs build")
    print("  2. Check: mkdocs serve")


if __name__ == "__main__":
    main()
