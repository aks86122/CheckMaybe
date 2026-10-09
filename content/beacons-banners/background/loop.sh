# usage: loop.sh IN START LEN XFADE CROPFILTER OUT
IN=$1; S=$2; L=$3; D=$4; CF=$5; OUT=$6
ffmpeg -v error -y -ss $S -t $(echo "$L+$D" | bc) -i $IN -an -filter_complex "
[0:v]$CF,setpts=PTS-STARTPTS,split=3[a][b][c];
[a]trim=start=$D:end=$L,setpts=PTS-STARTPTS[body];
[b]trim=start=$L:end=$(echo "$L+$D" | bc),setpts=PTS-STARTPTS[tail];
[c]trim=start=0:end=$D,setpts=PTS-STARTPTS[head];
[tail][head]xfade=transition=fade:duration=$D:offset=0[blend];
[body][blend]concat=n=2:v=1:a=0,format=yuv420p[v]" -map "[v]" -c:v libx264 -preset slow -crf 25 -profile:v high -movflags +faststart -r 30 $OUT
