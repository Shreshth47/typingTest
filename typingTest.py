import time
import requests

count = 0
total_chars_correct = 0

def randomWords():
  print("Please wait. Loading words...")
  print("\n")
  url= 'https://random-word-form.herokuapp.com/random/adjective?count=15'
  res = requests.get(url)
  para = res.json()
  return para

words = randomWords()

for k in words:
  print(k,end=" ") 
print("\n")

start_time = time.time()
user_input = input("Start Typing: \n")
end_time = time.time()
print("\n")

time_taken = end_time - start_time

inpWords = user_input.split(" ")

if(len(inpWords)!=15):
  print('You left few words. Try again!')
else:
  for i in range(min(len(words), len(inpWords))):
    if words[i] == inpWords[i]:
      total_chars_correct+=len(inpWords[i])
      total_chars_correct+=1
      count+=1
    
  speed = int((total_chars_correct*60)/(5*time_taken))
  print(f'Your typing speed is {speed} WPM!')
  print(f"Correct words: {count}/15")