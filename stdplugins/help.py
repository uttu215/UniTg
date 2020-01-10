import asyncio
from telethon import events


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):
                     input_str = event.pattern_match.group(1)
           if input_str == "help":
                    await event.reply("`"
                        "
account_profile

afk

alive

anime_download

anime

antiflood

aria

autopic

batch_upload

being_logical

bigf

bigspamreboot

blacklist

calendar

call_admin

carbon

chain

chandrayan2

channel_download

checker

chu

clock.animation

coinflip

colors

count

create_private_group

currency

dagd

decide

dictionary

download

Earth

emojis

eval

exec

fileext

filters

F

fullgaali

fullgali2

fun

fwd

gban

gbun

gdrive_download

get_admin

get_bot

get_id

github

gitupload

gmute

google

hack

_help

her

hypnotise

ifsc

imdb

instamusic

invite

jio

json

list

load

locks

log_pms

lydia_ai_chat_bot

markdown

meme

memify

moon.animation

music

netflix

ninja

ocr

ooof

openweathermap

pastebin

ping

pin_message

plane

pmpermit

police

polls

power_tools

profilepicgrab

promote

purge

__pycache__
qr_code

react

README.md
remove.bg

rename

rendi

sangmata

sca

schd

screencapture

sed

shoot

shout

slap

snake

snip

solarsystem

spam

speedtest

sp_search

stickers

sticklet

stt

tagall

telegraph

test2

test

thumbnail

time

torrent_search

torrentz

translate

tts

typewriter

ukinti

unbanmute

upload

upload_to_gDrive

upload_to_verystream

urbandictionary

welcome

whatscrapp

whois

wikimedia

wikipedia

xkcd

xtools

youtube_dl \n\n
To know the syntax and working of a particular module do .syntax module_name"
"`")

                    await event.delete()
