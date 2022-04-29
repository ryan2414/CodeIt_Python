import youtube_dl

ydl_opt = {
    # 'listformats': True # 다운로드 가능한 Option 보기
    'format': '18',
    'outtmpl': '%(title)s %(resolution)s.%(ext)s'
}

with youtube_dl.YoutubeDL(ydl_opt) as ydl:
    ydl.download(['https://youtu.be/siPVMYmDmEI'])
