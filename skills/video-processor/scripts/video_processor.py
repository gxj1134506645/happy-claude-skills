#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "click>=8.1.0",
#     "ffmpeg-python>=0.2.0",
#     "yt-dlp>=2024.0.0",
# ]
# ///

"""
Video Processor - A unified CLI tool for video/audio processing and transcription.

This script provides utilities for:
- Downloading videos from YouTube and other platforms
- Extracting audio from video files
- Converting videos to MP4 or WebM formats
- Transcribing audio/video using OpenAI's Whisper

Requirements:
- FFmpeg must be installed on the system
- OpenAI Whisper must be installed (pip install openai-whisper)
- yt-dlp must be installed (pip install yt-dlp)
"""

import os
import sys
import subprocess
import tempfile
from pathlib import Path
from typing import Optional

import click
import ffmpeg


def check_ffmpeg() -> bool:
    """Check if FFmpeg is installed and accessible."""
    try:
        subprocess.run(
            ["ffmpeg", "-version"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def check_whisper() -> bool:
    """Check if Whisper is installed and accessible."""
    try:
        subprocess.run(
            ["whisper", "--help"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def check_ytdlp() -> bool:
    """Check if yt-dlp is installed and accessible."""
    try:
        subprocess.run(
            ["yt-dlp", "--version"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def validate_input_file(file_path: str) -> Path:
    """Validate that the input file exists."""
    path = Path(file_path)
    if not path.exists():
        raise click.ClickException(f"Input file does not exist: {file_path}")
    if not path.is_file():
        raise click.ClickException(f"Input path is not a file: {file_path}")
    return path


@click.group()
@click.version_option(version="1.0.0")
def cli():
    """
    Video Processor - Process videos with FFmpeg and Whisper.

    A unified tool for video format conversion, audio extraction, and transcription.
    """
    pass


@cli.command()
@click.argument("url")
@click.argument("output_file", type=click.Path(), required=False)
@click.option(
    "--format",
    "video_format",
    default="best",
    help="Video format preference (default: best). Use 'bestvideo+bestaudio' for highest quality."
)
@click.option(
    "--audio-only",
    is_flag=True,
    help="Download audio only (no video)"
)
@click.option(
    "--subtitle",
    is_flag=True,
    help="Download subtitles if available"
)
@click.option(
    "--info",
    is_flag=True,
    help="Show video information without downloading"
)
def download(url: str, output_file: Optional[str], video_format: str, audio_only: bool, subtitle: bool, info: bool):
    """
    Download video from YouTube or other supported platforms using yt-dlp.

    Supports thousands of websites including YouTube, Vimeo, Twitter, etc.

    \b
    Examples:
        video_processor.py download "https://youtube.com/watch?v=..." output.mp4
        video_processor.py download "https://youtube.com/watch?v=..." --audio-only
        video_processor.py download "https://youtube.com/watch?v=..." --info
        video_processor.py download "https://youtube.com/watch?v=..." output.mp4 --subtitle
    """
    if not check_ytdlp():
        raise click.ClickException(
            "yt-dlp is not installed. Please install it:\n"
            "  pip install -U yt-dlp"
        )

    # Show info only
    if info:
        click.echo(f"Fetching video information from: {url}")
        try:
            result = subprocess.run(
                ["yt-dlp", "--print", "%(title)s\n%(uploader)s\n%(duration)s\n%(description)s", url],
                capture_output=True,
                text=True,
                check=True
            )
            lines = result.stdout.strip().split('\n')
            if len(lines) >= 3:
                click.echo(f"\nTitle: {lines[0]}")
                click.echo(f"Uploader: {lines[1]}")
                click.echo(f"Duration: {int(lines[2])//60}:{int(lines[2])%60:02d}")
                if len(lines) > 3:
                    click.echo(f"\nDescription:\n{lines[3][:500]}...")
            return
        except subprocess.CalledProcessError as e:
            raise click.ClickException(f"Failed to fetch video info:\n{e.stderr}")

    # Build yt-dlp command
    ytdlp_cmd = ["yt-dlp"]

    if audio_only:
        ytdlp_cmd.extend(["-x", "--audio-format", "mp3"])
        if output_file:
            ytdlp_cmd.extend(["-o", output_file])
        else:
            ytdlp_cmd.extend(["-o", "%(title)s.%(ext)s"])
    else:
        if video_format == "best":
            ytdlp_cmd.extend(["-f", "bestvideo+bestaudio/best"])
        else:
            ytdlp_cmd.extend(["-f", video_format])

        ytdlp_cmd.extend(["--merge-output-format", "mp4"])

        if output_file:
            ytdlp_cmd.extend(["-o", output_file])
        else:
            ytdlp_cmd.extend(["-o", "%(title)s.%(ext)s"])

    if subtitle:
        ytdlp_cmd.extend(["--write-sub", "--sub-lang", "en,zh-Hans,zh-Hant", "--embed-subs"])

    ytdlp_cmd.append(url)

    click.echo(f"Downloading from: {url}")
    if audio_only:
        click.echo("Mode: Audio only")
    else:
        click.echo(f"Format: {video_format}")

    try:
        subprocess.run(ytdlp_cmd, check=True)
        click.echo("✓ Download completed successfully!")

        # Find the downloaded file
        if output_file:
            output_path = Path(output_file)
            if output_path.exists():
                click.echo(f"Output: {output_path}")
                click.echo(f"File size: {output_path.stat().st_size / (1024*1024):.2f} MB")
    except subprocess.CalledProcessError as e:
        raise click.ClickException(f"yt-dlp download error: {str(e)}")


@cli.command()
@click.argument("input_file", type=click.Path(exists=True))
@click.argument("output_file", type=click.Path())
@click.option(
    "--format",
    default="wav",
    type=click.Choice(["wav", "mp3", "aac", "flac"], case_sensitive=False),
    help="Output audio format (default: wav)"
)
def extract_audio(input_file: str, output_file: str, format: str):
    """
    Extract audio from a video file.

    \b
    Examples:
        video_processor.py extract-audio video.mp4 audio.wav
        video_processor.py extract-audio video.mp4 audio.mp3 --format mp3
    """
    if not check_ffmpeg():
        raise click.ClickException(
            "FFmpeg is not installed. Please install it:\n"
            "  macOS: brew install ffmpeg\n"
            "  Ubuntu/Debian: apt-get install ffmpeg"
        )

    input_path = validate_input_file(input_file)
    output_path = Path(output_file)

    # Ensure output file has correct extension
    if not output_path.suffix:
        output_path = output_path.with_suffix(f".{format}")

    click.echo(f"Extracting audio from {input_path}...")
    click.echo(f"Output format: {format}")

    try:
        # Extract audio stream without video
        stream = ffmpeg.input(str(input_path))
        stream = ffmpeg.output(stream, str(output_path), acodec="pcm_s16le" if format == "wav" else format, vn=None)
        ffmpeg.run(stream, overwrite_output=True, capture_stdout=True, capture_stderr=True)

        click.echo(f"✓ Audio extracted successfully to {output_path}")
        click.echo(f"File size: {output_path.stat().st_size / (1024*1024):.2f} MB")
    except ffmpeg.Error as e:
        error_msg = e.stderr.decode() if e.stderr else str(e)
        raise click.ClickException(f"FFmpeg error during audio extraction:\n{error_msg}")


@cli.command()
@click.argument("input_file", type=click.Path(exists=True))
@click.argument("output_file", type=click.Path())
@click.option(
    "--codec",
    default="libx264",
    help="Video codec (default: libx264)"
)
@click.option(
    "--preset",
    default="medium",
    type=click.Choice(["ultrafast", "superfast", "veryfast", "faster", "fast", "medium", "slow", "slower", "veryslow"], case_sensitive=False),
    help="Encoding preset for speed/quality balance (default: medium)"
)
@click.option(
    "--crf",
    default=23,
    type=int,
    help="Constant Rate Factor for quality (default: 23, lower=better quality, range: 0-51)"
)
def to_mp4(input_file: str, output_file: str, codec: str, preset: str, crf: int):
    """
    Convert a video file to MP4 format.

    \b
    Examples:
        video_processor.py to-mp4 input.avi output.mp4
        video_processor.py to-mp4 input.mov output.mp4 --preset fast --crf 20
    """
    if not check_ffmpeg():
        raise click.ClickException(
            "FFmpeg is not installed. Please install it:\n"
            "  macOS: brew install ffmpeg\n"
            "  Ubuntu/Debian: apt-get install ffmpeg"
        )

    input_path = validate_input_file(input_file)
    output_path = Path(output_file)

    # Ensure output has .mp4 extension
    if output_path.suffix.lower() != ".mp4":
        output_path = output_path.with_suffix(".mp4")

    click.echo(f"Converting {input_path} to MP4...")
    click.echo(f"Codec: {codec}, Preset: {preset}, CRF: {crf}")

    try:
        stream = ffmpeg.input(str(input_path))
        stream = ffmpeg.output(
            stream,
            str(output_path),
            vcodec=codec,
            preset=preset,
            crf=crf,
            acodec="aac",
            audio_bitrate="128k"
        )
        ffmpeg.run(stream, overwrite_output=True, capture_stdout=True, capture_stderr=True)

        click.echo(f"✓ Video converted successfully to {output_path}")
        click.echo(f"File size: {output_path.stat().st_size / (1024*1024):.2f} MB")
    except ffmpeg.Error as e:
        error_msg = e.stderr.decode() if e.stderr else str(e)
        raise click.ClickException(f"FFmpeg error during MP4 conversion:\n{error_msg}")


@cli.command()
@click.argument("input_file", type=click.Path(exists=True))
@click.argument("output_file", type=click.Path())
@click.option(
    "--codec",
    default="libvpx-vp9",
    type=click.Choice(["libvpx", "libvpx-vp9"], case_sensitive=False),
    help="Video codec (default: libvpx-vp9 for VP9)"
)
@click.option(
    "--crf",
    default=30,
    type=int,
    help="Constant Rate Factor for quality (default: 30, lower=better quality, range: 0-63)"
)
@click.option(
    "--bitrate",
    default="1M",
    help="Target bitrate (default: 1M)"
)
def to_webm(input_file: str, output_file: str, codec: str, crf: int, bitrate: str):
    """
    Convert a video file to WebM format (web-optimized).

    \b
    Examples:
        video_processor.py to-webm input.mp4 output.webm
        video_processor.py to-webm input.avi output.webm --codec libvpx-vp9 --crf 25
    """
    if not check_ffmpeg():
        raise click.ClickException(
            "FFmpeg is not installed. Please install it:\n"
            "  macOS: brew install ffmpeg\n"
            "  Ubuntu/Debian: apt-get install ffmpeg"
        )

    input_path = validate_input_file(input_file)
    output_path = Path(output_file)

    # Ensure output has .webm extension
    if output_path.suffix.lower() != ".webm":
        output_path = output_path.with_suffix(".webm")

    click.echo(f"Converting {input_path} to WebM...")
    click.echo(f"Codec: {codec}, CRF: {crf}, Bitrate: {bitrate}")

    try:
        stream = ffmpeg.input(str(input_path))
        stream = ffmpeg.output(
            stream,
            str(output_path),
            vcodec=codec,
            crf=crf,
            acodec="libopus",
            audio_bitrate="128k",
            **{"b:v": bitrate}
        )
        ffmpeg.run(stream, overwrite_output=True, capture_stdout=True, capture_stderr=True)

        click.echo(f"✓ Video converted successfully to {output_path}")
        click.echo(f"File size: {output_path.stat().st_size / (1024*1024):.2f} MB")
    except ffmpeg.Error as e:
        error_msg = e.stderr.decode() if e.stderr else str(e)
        raise click.ClickException(f"FFmpeg error during WebM conversion:\n{error_msg}")


@cli.command()
@click.argument("input_file", type=click.Path(exists=True))
@click.argument("output_file", type=click.Path())
@click.option(
    "--model",
    default="base",
    type=click.Choice(["tiny", "base", "small", "medium", "large"], case_sensitive=False),
    help="Whisper model size (default: base)"
)
@click.option(
    "--language",
    default=None,
    help="Language code (e.g., en, es, fr). Auto-detect if not specified."
)
@click.option(
    "--format",
    "output_format",
    default="txt",
    type=click.Choice(["txt", "srt", "vtt", "json"], case_sensitive=False),
    help="Output format (default: txt)"
)
@click.option(
    "--verbose",
    is_flag=True,
    help="Show Whisper processing details"
)
def transcribe(input_file: str, output_file: str, model: str, language: Optional[str], output_format: str, verbose: bool):
    """
    Transcribe audio or video file using OpenAI's Whisper.

    If input is a video file, audio will be extracted automatically.

    \b
    Model sizes (speed vs accuracy):
      - tiny:   Fastest, lowest accuracy (~1GB RAM)
      - base:   Fast, good accuracy (~1GB RAM) [DEFAULT]
      - small:  Balanced (~2GB RAM)
      - medium: High accuracy (~5GB RAM)
      - large:  Best accuracy, slowest (~10GB RAM)

    \b
    Examples:
        video_processor.py transcribe video.mp4 transcript.txt
        video_processor.py transcribe audio.wav transcript.srt --format srt --model small
        video_processor.py transcribe interview.mp4 transcript.txt --model medium --language es
    """
    if not check_ffmpeg():
        raise click.ClickException(
            "FFmpeg is not installed. Please install it:\n"
            "  macOS: brew install ffmpeg\n"
            "  Ubuntu/Debian: apt-get install ffmpeg"
        )

    if not check_whisper():
        raise click.ClickException(
            "OpenAI Whisper is not installed. Please install it:\n"
            "  pip install -U openai-whisper"
        )

    input_path = validate_input_file(input_file)
    output_path = Path(output_file)

    # Determine if we need to extract audio first
    video_extensions = {".mp4", ".avi", ".mov", ".mkv", ".webm", ".flv", ".wmv"}
    audio_extensions = {".wav", ".mp3", ".aac", ".flac", ".m4a", ".ogg"}

    temp_audio = None
    audio_file = input_path

    if input_path.suffix.lower() in video_extensions:
        click.echo(f"Input is video file - extracting audio first...")
        # Create temporary WAV file for Whisper
        temp_audio = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
        temp_audio.close()
        audio_file = Path(temp_audio.name)

        try:
            # Extract audio to temporary file optimized for Whisper (16kHz mono)
            stream = ffmpeg.input(str(input_path))
            stream = ffmpeg.output(stream, str(audio_file), acodec="pcm_s16le", ac=1, ar="16000", vn=None)
            ffmpeg.run(stream, overwrite_output=True, capture_stdout=True, capture_stderr=True)
            click.echo(f"✓ Audio extracted to temporary file")
        except ffmpeg.Error as e:
            if temp_audio:
                os.unlink(audio_file)
            error_msg = e.stderr.decode() if e.stderr else str(e)
            raise click.ClickException(f"FFmpeg error during audio extraction:\n{error_msg}")
    elif input_path.suffix.lower() not in audio_extensions:
        raise click.ClickException(
            f"Unsupported file format: {input_path.suffix}\n"
            f"Supported video: {', '.join(video_extensions)}\n"
            f"Supported audio: {', '.join(audio_extensions)}"
        )

    # Run Whisper transcription
    click.echo(f"Transcribing with Whisper (model: {model})...")
    if language:
        click.echo(f"Language: {language}")
    else:
        click.echo("Language: auto-detect")

    try:
        # Build Whisper command
        whisper_cmd = [
            "whisper",
            str(audio_file),
            "--model", model,
            "--output_format", output_format,
            "--output_dir", str(output_path.parent if output_path.parent.exists() else Path.cwd())
        ]

        if language:
            whisper_cmd.extend(["--language", language])

        if not verbose:
            whisper_cmd.append("--verbose")
            whisper_cmd.append("False")

        # Run Whisper
        result = subprocess.run(
            whisper_cmd,
            capture_output=not verbose,
            text=True,
            check=True
        )

        # Whisper creates output with original filename - rename to desired output
        whisper_output = audio_file.parent / f"{audio_file.stem}.{output_format}"

        # If Whisper output is in a different location, find it
        if not whisper_output.exists():
            # Check in output directory
            output_dir = output_path.parent if output_path.parent.exists() else Path.cwd()
            whisper_output = output_dir / f"{audio_file.stem}.{output_format}"

        if whisper_output.exists() and whisper_output != output_path:
            whisper_output.rename(output_path)

        click.echo(f"✓ Transcription completed successfully!")
        click.echo(f"Output: {output_path}")

        if output_path.exists():
            click.echo(f"File size: {output_path.stat().st_size / 1024:.2f} KB")

            # Show preview for text formats
            if output_format == "txt" and output_path.stat().st_size < 5000:
                click.echo("\nPreview:")
                click.echo("-" * 50)
                with open(output_path, "r", encoding="utf-8") as f:
                    preview = f.read(500)
                    click.echo(preview)
                    if len(preview) >= 500:
                        click.echo("...")
                click.echo("-" * 50)

    except subprocess.CalledProcessError as e:
        error_msg = e.stderr if e.stderr else str(e)
        raise click.ClickException(f"Whisper transcription error:\n{error_msg}")
    finally:
        # Clean up temporary audio file
        if temp_audio and audio_file.exists():
            try:
                os.unlink(audio_file)
                click.echo("✓ Temporary audio file cleaned up")
            except Exception:
                pass  # Best effort cleanup


if __name__ == "__main__":
    cli()
