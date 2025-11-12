import streamlit as st

with st.sidebar:
	image = 'soobin_hoang_son.webp'
	st.image(image, caption='Soobin Hoàng Sơn')
	st.write('Họ và tên: Nguyễn Huỳnh Sơn ')
	st.write('Nghệ danh: Soobin Hoàng Sơn')
	st.write('Nguyễn Huỳnh Sơn,thường được biết đến với nghệ danh\
Soobin Hoàng Sơn hay Soobin, là một nam ca sĩ kiêm nhà sáng tác âm nhạc\
và là một rapper nổi tiếng của nhóm nhạc spacespeaker. Soobin từng đạt giải làn sóng xanh\
và nhiều các danh hiệu khác và có bố là một nghệ sĩ nhân dân nổi tiếng.')
	

st.title('Bài hát yêu thích')
st.write('Giá như')
audio = open('gia_nhu.mp3', 'rb')
st.audio(audio, format='audio/mp3')

st.title('MV yêu thích')
st.write('Phía Sau Một Cô Gái')
video = 'https://www.youtube.com/watch?v=vCIc1g_4JWM'
st.video(video, format='video/m4')