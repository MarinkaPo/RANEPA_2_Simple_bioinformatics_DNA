######################
# Import
######################

import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

######################
# Для заголовка страницы
######################

st.write("""
# Простое приложение для подсчёта кол-ва нуклеотидов в ДНК
Задаёте цепочку ДНК -> считает количество нуклеотидов
""")

image = Image.open('DNA.png')
st.image(image, use_column_width=True)

######################
# Для ввода цепочки
######################

#st.sidebar.header('Enter DNA sequence')
st.header('Введите последовательность ДНК')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

#sequence = st.sidebar.text_area("Sequence input", sequence_input, height=250)
sequence = st.text_area("Введённая последовательность: ", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:] # Skips the sequence name (first line)
sequence = ''.join(sequence) # Concatenates list to string

st.write("""
******************
""")

## Посмотрим последовательность:
st.header('Введённая последовательность:')
sequence

## Считаем:
st.header('Подсчёт нуклеотидов:')

### 1. Получили словарь
st.subheader('1. Получили такой словарь:')
def DNA_nucleotide_count(seq):
  d = dict([
            ('A',seq.count('A')),
            ('T',seq.count('T')),
            ('G',seq.count('G')),
            ('C',seq.count('C'))
            ])
  return d

X = DNA_nucleotide_count(sequence)

#X_label = list(X)
#X_values = list(X.values())

X

### 2. Итого:
st.subheader('2. Итого:')
st.write('Найдено  ' + str(X['A']) + ' аденина (A)')
st.write('Найдено  ' + str(X['T']) + ' тимина (T)')
st.write('Найдено  ' + str(X['G']) + ' гуанина (G)')
st.write('Найдено  ' + str(X['C']) + ' цитозина (C)')

### 3. Смотрим в виде датафрейма
st.subheader('3. Смотрим в виде датафрейма:')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'количество'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'нуклеотид'})
st.write(df)

### 4. График распределения нуклеотидов с помощью Altair
st.subheader('4. Смотрим график:')
p = alt.Chart(df).mark_bar().encode(
    x='нуклеотид',
    y='количество'
)
p = p.properties(
    width=alt.Step(80)  # controls width of bar.
)
st.write(p)
