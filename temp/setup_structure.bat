@echo off

REM Creating the sub-directories
mkdir data
mkdir data\raw
mkdir data\audio
mkdir data\transcripts

mkdir models
mkdir models\whisper_configs

mkdir src
mkdir src\downloader
mkdir src\processing
mkdir src\transcriber
mkdir src\timestamp_generator
mkdir src\utils

mkdir tests

mkdir logs

mkdir config

mkdir scripts

mkdir notebooks

REM Creating placeholder files
echo # Project Overview > README.md
echo # License Information > LICENSE
echo # This file contains all required dependencies > requirements.txt

REM Creating basic config file
echo default_model: "base" > config\config.yaml

echo Folder structure successfully created!
