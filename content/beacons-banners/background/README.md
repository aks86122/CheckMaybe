# Beacons background videos (12 s seamless loops, no audio)

Source: two Pexels videos the founder downloaded at 960x540 (Pexels License: free commercial use, no attribution required).
- taipei-sunset-*: Pexels video 8669846 (Taipei 101 sunset timelapse), from 0:03
- night-bridge-*: Pexels video 13825990 (night aerial over a lit bridge and park), from 0:04

| File | Use | Size |
| --- | --- | --- |
| *-vertical.mp4 (540x960) | Beacons background on phones (most visitors) | ~1 MB |
| *-landscape.mp4 (960x540) | Desktop, if Beacons asks for a separate desktop background | ~1–1.5 MB |

Loops are made by `loop.sh`: the last 1.5 s cross-fade into the first 1.5 s, so the restart has no jump.
The vertical crop is upscaled from 304x540, so it is slightly soft; behind 80% opaque cards that does not show. For a sharper one, download the 1920x1080 version and re-run loop.sh.
