import pyttsx3 
import datetime
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)




def speak (audio):
	engine.say(audio)
	engine.runAndWait()


def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		speak("Good Morning sir , have a nice day!!")
	elif hour >=12 and hour<18:
		speak('Good Afternoon sir')
	else:
		speak('Good Evening sir')
	speak(' i am Jarvis!.. , Your personal assistance!.., ,sir, How can I Help You')




	
if __name__ == '__main__':
	wishMe()
	query=input('type your first query : ')
	#while True:
	if 1:


		#Logic for executing tasks based on query
		if 'wikipedia' in query:
			speak('searching wikipedia...')
			query = query.replace('wikipedia', '')
			results = wikipedia.summary(query , sentences=2)
			speak('According to wikipedia')
			print(results)
			speak(results)

		


		elif 'open youtube' in query:
			speak(f'wait sir i am opening your task')
			webbrowser.open('youtube.com')
			

		elif 'open google' in query:
			speak(f'wait sir i am opening your task')
			webbrowser.open('google.com')
			

		elif 'open acpc' in query:
			speak(f'wait sir i am opening your task')
			webbrowser.open('gujacpc.nic.in')

		elif 'time' in query:
			strTime = datetime.datetime.now().strftime('%H:%M:%S \n %D')
			time = 'clock.py'
			os.startfile(time)
			speak(f'sir, the time is {strTime}')
			

		elif 'sublime' in query:
			codepath='C:\\Program Files\\Sublime Text 3\\sublime_text.exe'
			os.startfile(codepath)

		elif 'time' in query:
			strTime = datetime.datetime.now().strftime('%H:%M:%S \n %D')
			time = 'clock.py'
			os.startfile(time)
			speak(f'sir, the time is {strTime}')
		
		elif 'python' in query:
			pythonpath = 'C:\\Users\\krishna\\AppData\\Local\\Programs\\Python\\Python38-32\\pythonw.exe "C:\\Users\\krishna\\AppData\\Local\\Programs\\Python\\Python38-32\\Lib\\idlelib\\idle.pyw'
			speak(f'wair sir, i am opening your task')

		elif 'vashishth photo' in query:
			imagepath = 'my photo.jpg'
			speak(f'sir , your image is ready')
			os.startfile(imagepath)


		elif 'net protector' in query:
			netpath = "C:\\Program Files\\Net Protector 2020\\ZVSCAN\\ZEROVSCN.EXE"
			speak(f'sir, your task is ready')
			os.startfile(netpath)
		
                
		elif 'aditi photo' in query:
			speak(f'sir, aditi`s photo is ready')
			imagepath2 = 'aditi.jpg'
			os.startfile(imagepath2)

		elif 'papa photo' in query:
			speak(f'honorable,  papa`s photo is ready')
			imagepath3 = 'papa.jpg'
			os.startfile(imagepath3)

		elif 'mummy photo' in query:
			speak(f'honorable,  mummy`s image is ready')	
			imagepath4 = 'mummy.jpg'
			os.startfile(imagepath4)

		elif 'music' in query:
				speak(f'sir! , which music , you want to play ?')
				print('1.Abuzada \n2.Ambarasiya \n3.chainsmooker \n4.daru badnam \n5.Despacito \n6.Gaman santhal \n7.Gangland \n8.imagin dragon \n9.Kapil sharma \n10.Kinjal dave \n11.Kirtidan gadhavi \n12.Maula mere lele meri jaan \n13.Mitwa \n14.On my way \n15.Pal pal dil ke paas \n16.Phir mohabbat \n17.Photo song \n18.Sakhiyana song \n19.She move it like \n20.Tere bin nahi laage jiya \n21.Tum aaoge mujhe milne  \n22.Vijay suvada \n23.Yaar ki shaadi ')
				speak(f'type a, song number')
				song = input('type a number: ')
				if '1' == song:
					print('you want to play Abuzada')
					speak(f'music!..')
					song1 = 'music\\abuzada.mp3'
					os.startfile(song1)
				elif  '2' == song:
					print('you want to play Ambarasiya')
					speak(f'music!..')
					song2 = 'music\\ambarasiya.m4a'
					os.startfile(song2)
				elif '3' == song:
					print('you want to play Chainsmooker')
					speak(f'music!..')
					song3 = 'music\\chainsmooker.mp3'
					os.startfile(song3)
				elif '4' == song:
					print('you want to play Daru badnam')
					speak(f'music!..')
					song4 = 'music\\daru badnam.m4a'
					os.startfile(song4)
				elif '5' == song:
					print('you want to play Despacito')
					speak(f'music!..')
					song5 = 'music\\despacito.m4a'
					os.startfile(song5)
				elif '6' == song:
					print('you want to play Gaman santhal')
					speak(f'music!..')
					song6 = 'music\\gaman santhal.m4a'
					os.startfile(song6)
				elif '7' == song:
					print('you want to play Gangland')
					speak(f'music!..')
					song7 = 'music\\gangland.mp4'
					os.startfile(song7)
				elif '8' == song:
					print('you want to play imagin dragon')
					speak(f'music!..')
					song8 = 'music\\imagin dragon.mp3'
					os.startfile(song8)
				elif '9' == song:
					print('you want to play the kapil sharma show..')
					speak(f'music..')
					song9 ='music\\kapil sharma.mp4'
					os.startfile(song9)
				elif  '10' == song:
					print('you want to play Kinjal dave song')
					speak(f'music')
					song10 = 'music\\kinjal dave.mp3'
					os.startfile(song10)
				elif '11' == song:
					print('you want to play Kirtidan gadhavi')
					speak(f'music..')
					song11 = 'music\\kirtidan gadhavi.mp3'
					os.startfile(song11)
				elif '12' == song:
					speak(f'music..')
					print('you want to play maula mere lele meri jan..')
					song12 = 'music\\maula mere lele meri jan.m4a'
					os.startfile(song12)
				elif '13' == song:
					print('you want to play mitwa song...')
					speak(f'music..')
					song13 = 'music\\mitwa.mp3'
					os.startfile(song13)
				elif '14' == song:
					print('you want to play on my way...')
					speak(f'music..')
					song14 = 'music\\on my way.m4a'
					os.startfile(song14)
				elif '15' == song:
					print('you want to play pal pal dil ke paas..')
					speak(f'music..')
					song15 = 'music\\pal pal dil ke pas.mp3'
					os.startfile(song15)
				elif '16' == song:
					print('you want to play phir mohabbat...')
					speak(f'music...')
					song16 = 'music\\phir mohabbat.m4a'
					os.startfile(song16)
				elif '17' ==song:
					print('you want to play photo song...')
					speak(f'music...')
					song17 = 'music\\photo song.mp3'
					os.startfile(song17)
				elif '18' == song:
					print('you want to play sakhiyana song...')
					speak(f'music..')
					song18 = 'music\\sakhiyana.mp3'
					os.startfile(song18)
				elif '19' == song:
					print('you want to play she move it like...')
					speak(f'music..')
					song19 = 'music\\she move it like.mp3'
					os.startfile(song19)
				elif '20' == song:
					print('you want to play tere bin nahi laage jiya..')
					speak(f'music...')
					song20 = 'music\\tere bin nahi laaage jiya.mp3'
					os.startfile(song20)
				elif '21' == song:
					print('you want to play tum aaoge mujhe milne..')
					speak(f'music...')
					song21 = 'music\\tum aaaoge mujhe milne.m4a'
					os.startfile(song21)
				elif '22' == song:
					print('you want to play vijay suvada song... ')
					speak(f'music..')
					song22 = 'music\\vijay suvada.mp3'
					os.startfile(song22)
				elif '23' == song:
					print('you want to play yaar ki shaadi song...')
					speak(f'music...')
					song23 = 'music\\yaaar ki shaadi.mp3'
					os.startfile(song23)
				else:
					print('this song is not available...')
					speak(f'this song is not available...')

				
                                              
                                        
				
				               
	if 2:
		speak(f'sir , do you want to run one another task? ')
		answer = input('yes or no : ')
		if 'yes' in answer:
			speak(f'nice sir! , what you want to do? ')
			query1 = input('type your second query: ')
			if 'wikipedia' in query1:
				speak('searching wikipedia...')
				query = query.replace('wikipedia', '')
				results = wikipedia.summary(query , sentences=2)
				speak('According to wikipedia')
				print(results)
				speak(results)


			elif 'open youtube' in query1:        
				speak(f'wait sir i am opening your task')
				webbrowser.open('youtube.com')
			

			elif 'open google' in query1:
				speak(f'wait sir i am opening your task')
				webbrowser.open('google.com')

			
			elif 'open acpc' in query1:
				speak(f'wait sir i am opening your task')
				webbrowser.open('gujacpc.nic.in')
			

			elif 'sublime' in query1:
				codepath='C:\\Program Files\\Sublime Text 3\\sublime_text.exe'
				os.startfile(codepath)

			elif 'time' in query1:
				strTime = datetime.datetime.now().strftime('%H:%M:%S \n %D')
				time = 'clock.py'
				os.startfile(time)
				speak(f'sir, the time is {strTime}')
		
			elif 'python' in query1:
				pythonpath = 'C:\\Users\\krishna\\AppData\\Local\\Programs\\Python\\Python38-32\\pythonw.exe "C:\\Users\\krishna\\AppData\\Local\\Programs\\Python\\Python38-32\\Lib\\idlelib\\idle.pyw'
				speak(f'wair sir, i am opening your task')

			elif 'vashishth photo'  in query1:
				imagepath = 'my photo.jpg'
				speak(f'sir , your image is ready')
				os.startfile(imagepath)


			elif 'net protector' in query1:
				netpath = "C:\\Program Files\\Net Protector 2020\\ZVSCAN\\ZEROVSCN.EXE"
				speak(f'sir, your task is ready')
				os.startfile(netpath)


			elif 'aditi photo'  in query1:
				speak(f'sir, aditi`s photo is ready')
				imagepath2 = 'aditi.jpg'
				os.startfile(imagepath2)

			elif 'papa photo' in query1:
				speak(f'honorable,  papa`s photo is ready')
				imagepath3 = 'papa.jpg'
				os.startfile(imagepath3)

			elif 'mummy photo'  in query1:
				speak(f'honorable,  mummy`s image is ready')	
				imagepath4 = 'mummy.jpg'
				os.startfile(imagepath4)

			elif 'music' or 'song' or 'play music' in query1:
				speak(f'sir! , which music , you want to play ?')
				print('1.Abuzada \n2.Ambarasiya \n3.chainsmooker \n4.daru badnam \n5.Despacito \n6.Gaman santhal \n7.Gangland \n8.imagin dragon \n9.Kapil sharma \n10.Kinjal dave \n11.Kirtidan gadhavi \n12.Maula mere lele meri jaan \n13.Mitwa \n14.On my way \n15.Pal pal dil ke paas \n16.Phir mohabbat \n17.Photo song \n18.Photo song \n19.Sakhiyana song \n20.She move it like \n21.Tere bin nahi laage jiya \n22.Tum aaoge mujhe milne  \n23.Vijay suvada \n24.Yaar ki shaadi ')
				speak(f'type a, song number')
				song = input('type a number: ')
				if '1' == song:
					print('you want to play Abuzada')
					speak(f'music!..')
					song1 = 'music\\abuzada.mp3'
					os.startfile(song1)
				elif  '2' == song:
					print('you want to play Ambarasiya')
					speak(f'music!..')
					song2 = 'music\\ambarasiya.m4a'
					os.startfile(song2)
				elif '3' == song:
					print('you want to play Chainsmooker')
					speak(f'music!..')
					song3 = 'music\\chainsmooker.mp3'
					os.startfile(song3)
				elif '4' == song:
					print('you want to play Daru badnam')
					speak(f'music!..')
					song4 = 'music\\daru badnam.m4a'
					os.startfile(song4)
				elif '5' == song:
					print('you want to play Despacito')
					speak(f'music!..')
					song5 = 'music\\despacito.m4a'
					os.startfile(song5)
				elif '6' == song:
					print('you want to play Gaman santhal')
					speak(f'music!..')
					song6 = 'music\\gaman santhal.m4a'
					os.startfile(song6)
				elif '7' == song:
					print('you want to play Gangland')
					speak(f'music!..')
					song7 = 'music\\gangland.mp4'
					os.startfile(song7)
				elif '8' == song:
					print('you want to play imagin dragon')
					speak(f'music!..')
					song8 = 'music\\imagin dragon.mp3'
					os.startfile(song8)
				elif '9' == song:
					print('you want to play the kapil sharma show..')
					speak(f'music..')
					song9 ='music\\kapil sharma.mp4'
					os.startfile(song9)
				elif  '10' == song:
					print('you want to play Kinjal dave song')
					speak(f'music')
					song10 = 'music\\kinjal dave.mp3'
					os.startfile(song10)
				elif '11' == song:
					print('you want to play Kirtidan gadhavi')
					speak(f'music..')
					song11 = 'music\\kirtidan gadhavi.mp3'
					os.startfile(song11)
				elif '12' == song:
					speak(f'music..')
					print('you want to play maula mere lele meri jan..')
					song12 = 'music\\maula mere lele meri jan.m4a'
					os.startfile(song12)
				elif '13' == song:
					print('you want to play mitwa song...')
					speak(f'music..')
					song13 = 'music\\mitwa.mp3'
					os.startfile(song13)
				elif '14' == song:
					print('you want to play on my way...')
					speak(f'music..')
					song14 = 'music\\on my way.m4a'
					os.startfile(song14)
				elif '15' == song:
					print('you want to play pal pal dil ke paas..')
					speak(f'music..')
					song15 = 'music\\pal pal dil ke pas.mp3'
					os.startfile(song15)
				elif '16' == song:
					print('you want to play phir mohabbat...')
					speak(f'music...')
					song16 = 'music\\phir mohabbat.m4a'
					os.startfile(song16)
				elif '17' ==song:
					print('you want to play photo song...')
					speak(f'music...')
					song17 = 'music\\photo song.mp3'
					os.startfile(song17)
				elif '18' == song:
					print('you want to play sakhiyana song...')
					speak(f'music..')
					song18 = 'music\\sakhiyana.mp3'
					os.startfile(song18)
				elif '19' == song:
					print('you want to play she move it like...')
					speak(f'music..')
					song19 = 'music\\she move it like.mp3'
					os.startfile(song19)
				elif '20' == song:
					print('you want to play tere bin nahi laage jiya..')
					speak(f'music...')
					song20 = 'music\\tere bin nahi laaage jiya.mp3'
					os.startfile(song20)
				elif '21' == song:
					print('you want to play tum aaoge mujhe milne..')
					speak(f'music...')
					song21 = 'music\\tum aaaoge mujhe milne.m4a'
					os.startfile(song21)
				elif '22' == song:
					print('you want to play vijay suvada song... ')
					speak(f'music..')
					song22 = 'music\\vijay suvada.mp3'
					os.startfile(song22)
				elif '23' == song:
					print('you want to play yaar ki shaadi song...')
					speak(f'music...')
					song23 = 'music\\yaaar ki shaadi.mp3'
					os.startfile(song23)
				else:
					print('this song is not available...')
					speak(f'this song is not available...')
				
                                
		elif 'no' in answer:
			speak(f'ok sir! , thanks for your important time')

	











	
			

  
