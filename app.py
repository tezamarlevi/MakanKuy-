import streamlit as st
import pandas as pd
from PIL import Image
import gensim
from nltk import tokenize
from nltk.cluster.util import cosine_distance
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from wordcloud import WordCloud
from gensim.models import Word2Vec

df = pd.read_csv('tesimages.csv')
pageicon = Image.open('MakanKuy!.png')
foot = Image.open('footer2.png')
side2=Image.open('side2.jpg')
side3=Image.open('side4.jpg')
home1=Image.open('home6.png')
home2=Image.open('home7.jpg')
home3=Image.open('home10.jpg')
home4=Image.open('home11.jpg')
home5=Image.open('home12.jpg')
home6=Image.open('home13.jpg')
home7=Image.open('home1.jpg')
home8=Image.open('home15.jpg')
home9=Image.open('home16.jpg')


st.set_page_config(
    page_title="MAKAN KUY!",
    page_icon=pageicon,
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.github.com/reynaldimarchiano',
        'Report a bug': "https://www.google.com",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

header = Image.open('header.png')
header2 = Image.open('welcome3.png')
# header2 = header2.resize((1300,300))
st.image('header.png', use_column_width=True)
st.subheader('Makankuy! adalah sebuah aplikasi pemesanan tempat makan terdekat, yang dapat memberikan rekomendasi berdasarkan suasana yang diinginkan oleh customer serta preferensi tempat makan yang telah diketahui customer.')
st.write('-----')

opsi =st.sidebar.selectbox('MENU', ['Beranda', 'Rekomendasi Berdasarkan Keinginan', 'Rekomendasi Berdasarkan Referenso Tempat'])
st.sidebar.image('MakanKuy!2.png', width=300)
# st.sidebar.image('side2.jpg', width=300)
st.sidebar.image(side3, width=300)

#FLOW 1
model_2 = gensim.models.Word2Vec.load('model_2.model')
data = pd.read_csv('df_percent.csv')
def input_text(text1, text2, text3):
  list_new =[]
  columns_new= []
  count_word_1 = []
  count_word_2 = []
  count_word_3 = []
  count_word_4 = []
  count_word_5 = []
  count_word_6 = []
  count_word_7 = []
  count_word_8 = []
  count_word_9 = []
  count_word_10 = []
  count_word_11 = []
  count_word_12 = []
  count_word_13 = []
  count_word_14 = []
  count_word_15 = []

  try:
    # Jika bisa semuanya
    res_1 = model_2.wv.ost_similar(text1)[0:5]   
    res_2 = model_2.wv.ost_similar(text2)[0:5]
    res_3 = model_2.wv.ost_similar(text3)[0:5]
    df_res_1 = pd.DataFrame(res_1)
    df_res_2 = pd.DataFrame(res_2)
    df_res_3 = pd.DataFrame(res_3)
    df_result_1 = pd.concat([df_res_1, df_res_2, df_res_3], axis=0).reset_index(drop=True)
    for item in df_result_1[0].unique():
      list_new.append(item)
    for i in range(len(data)):
      count_word_1.append(data['clean stopword'][i].count(list_new[0]))
      count_word_2.append(data['clean stopword'][i].count(list_new[1]))
      count_word_3.append(data['clean stopword'][i].count(list_new[2]))
      count_word_4.append(data['clean stopword'][i].count(list_new[3]))
      count_word_5.append(data['clean stopword'][i].count(list_new[4]))
      count_word_6.append(data['clean stopword'][i].count(list_new[5]))
      count_word_7.append(data['clean stopword'][i].count(list_new[6]))
      count_word_8.append(data['clean stopword'][i].count(list_new[7]))
      count_word_9.append(data['clean stopword'][i].count(list_new[8]))
      count_word_10.append(data['clean stopword'][i].count(list_new[9]))
      count_word_11.append(data['clean stopword'][i].count(list_new[10]))
      count_word_12.append(data['clean stopword'][i].count(list_new[11]))
      count_word_13.append(data['clean stopword'][i].count(list_new[12]))
      count_word_14.append(data['clean stopword'][i].count(list_new[13]))
      count_word_15.append(data['clean stopword'][i].count(list_new[14]))
    data['count_word_1'] = count_word_1
    data['count_word_2'] = count_word_2
    data['count_word_3'] = count_word_3
    data['count_word_4'] = count_word_4
    data['count_word_5'] = count_word_5
    data['count_word_6'] = count_word_6
    data['count_word_7'] = count_word_7
    data['count_word_8'] = count_word_8
    data['count_word_9'] = count_word_9
    data['count_word_10'] = count_word_10
    data['count_word_11'] = count_word_11
    data['count_word_12'] = count_word_12
    data['count_word_13'] = count_word_13
    data['count_word_14'] = count_word_14
    data['count_word_15'] = count_word_15
    data['sum_count_word'] = data.iloc[:,11:25].sum(axis=1)
    data_1 = data[data.sum_count_word != 0]
    data_1 = data_1.sort_values("sum_count_word", ascending=False)[['Nama','Tipe_1', 'Rating', 'Price', 'Daerah', 'sum_count_word']]
    return data_1

  except:
    try:
      # Hanya 2 dan 3
      res_2 = model_2.wv.most_similar(text2)[0:5]
      res_3 = model_2.wv.most_similar(text3)[0:5]
      df_res_2 = pd.DataFrame(res_2)
      df_res_3 = pd.DataFrame(res_3)
      df_result_2 = pd.concat([df_res_2, df_res_3], axis=0).reset_index(drop=True)
      for item in df_result_2[0].unique():
        list_new.append(item)
      for i in range(len(data)):
        count_word_1.append(data['clean stopword'][i].count(list_new[0]))
        count_word_2.append(data['clean stopword'][i].count(list_new[1]))
        count_word_3.append(data['clean stopword'][i].count(list_new[2]))
        count_word_4.append(data['clean stopword'][i].count(list_new[3]))
        count_word_5.append(data['clean stopword'][i].count(list_new[4]))
        count_word_6.append(data['clean stopword'][i].count(list_new[5]))
        count_word_7.append(data['clean stopword'][i].count(list_new[6]))
        count_word_8.append(data['clean stopword'][i].count(list_new[7]))
        count_word_9.append(data['clean stopword'][i].count(list_new[8]))
        count_word_10.append(data['clean stopword'][i].count(list_new[9]))
      data['count_word_1'] = count_word_1
      data['count_word_2'] = count_word_2
      data['count_word_3'] = count_word_3
      data['count_word_4'] = count_word_4
      data['count_word_5'] = count_word_5
      data['count_word_6'] = count_word_6
      data['count_word_7'] = count_word_7
      data['count_word_8'] = count_word_8
      data['count_word_9'] = count_word_9
      data['count_word_10'] = count_word_10
      data['sum_count_word'] = data.iloc[:,11:20].sum(axis=1)
      data_2 = data[data.sum_count_word != 0]
      data_2 = data_2.sort_values("sum_count_word", ascending=False)[['Nama','Tipe_1', 'Rating', 'Price', 'Daerah', 'sum_count_word']]
      return data_2

    except:
      try:
        # Hanya 3 
        res_3 = model_2.wv.most_similar(text3)[0:5]
        df_result_3 = pd.DataFrame(res_3).reset_index(drop=True)
        for item in df_result_3[0].unique():
          list_new.append(item)
        for i in range(len(data)):
          count_word_1.append(data['clean stopword'][i].count(list_new[0]))
          count_word_2.append(data['clean stopword'][i].count(list_new[1]))
          count_word_3.append(data['clean stopword'][i].count(list_new[2]))
          count_word_4.append(data['clean stopword'][i].count(list_new[3]))
          count_word_5.append(data['clean stopword'][i].count(list_new[4]))
        data['count_word_1'] = count_word_1
        data['count_word_2'] = count_word_2
        data['count_word_3'] = count_word_3
        data['count_word_4'] = count_word_4
        data['count_word_5'] = count_word_5
        data['sum_count_word'] = data.iloc[:,11:15].sum(axis=1)
        data_3 = data[data.sum_count_word != 0]
        data_3 = data_3.sort_values("sum_count_word", ascending=False)[['Nama','Tipe_1', 'Rating', 'Price', 'Daerah', 'sum_count_word']]
        return data_3

      except :
        try:
          # Hanya 1 dan 2
          res_1 = model_2.wv.most_similar(text1)[0:5]
          res_2 = model_2.wv.most_similar(text2)[0:5]
          df_res_1 = pd.DataFrame(res_1)
          df_res_2 = pd.DataFrame(res_2)
          df_result_4 = pd.concat([df_res_1, df_res_2], axis=0).reset_index(drop=True)
          for item in df_result_4[0].unique():
            list_new.append(item)
          for i in range(len(data)):
            count_word_1.append(data['clean stopword'][i].count(list_new[0]))
            count_word_2.append(data['clean stopword'][i].count(list_new[1]))
            count_word_3.append(data['clean stopword'][i].count(list_new[2]))
            count_word_4.append(data['clean stopword'][i].count(list_new[3]))
            count_word_5.append(data['clean stopword'][i].count(list_new[4]))
            count_word_6.append(data['clean stopword'][i].count(list_new[5]))
            count_word_7.append(data['clean stopword'][i].count(list_new[6]))
            count_word_8.append(data['clean stopword'][i].count(list_new[7]))
            count_word_9.append(data['clean stopword'][i].count(list_new[8]))
            count_word_10.append(data['clean stopword'][i].count(list_new[9]))
          data['count_word_1'] = count_word_1
          data['count_word_2'] = count_word_2
          data['count_word_3'] = count_word_3
          data['count_word_4'] = count_word_4
          data['count_word_5'] = count_word_5
          data['count_word_6'] = count_word_6
          data['count_word_7'] = count_word_7
          data['count_word_8'] = count_word_8
          data['count_word_9'] = count_word_9
          data['count_word_10'] = count_word_10
          data['sum_count_word'] = data.iloc[:,11:20].sum(axis=1)
          data_4 = data[data.sum_count_word != 0]
          data_4 = data_4.sort_values("sum_count_word", ascending=False)[['Nama','Tipe_1', 'Rating', 'Price', 'Daerah', 'sum_count_word']]
          return data_4

        except:
          try:
            # Hanya res 2 
            res_2 = model_2.wv.most_similar(text2)[0:5]
            df_res_2 = pd.DataFrame(res_2)
            df_result_5 = df_res_2.reset_index(drop=True)
            for item in df_result_5[0].unique():
              list_new.append(item)
            for i in range(len(data)):
              count_word_1.append(data['clean stopword'][i].count(list_new[0]))
              count_word_2.append(data['clean stopword'][i].count(list_new[1]))
              count_word_3.append(data['clean stopword'][i].count(list_new[2]))
              count_word_4.append(data['clean stopword'][i].count(list_new[3]))
              count_word_5.append(data['clean stopword'][i].count(list_new[4]))
            data['count_word_1'] = count_word_1
            data['count_word_2'] = count_word_2
            data['count_word_3'] = count_word_3
            data['count_word_4'] = count_word_4
            data['count_word_5'] = count_word_5
            data['sum_count_word'] = data.iloc[:,11:15].sum(axis=1)
            data_5 = data[data.sum_count_word != 0]
            data_5 = data_5.sort_values("sum_count_word", ascending=False)[['Nama','Tipe_1', 'Rating', 'Price', 'Daerah', 'sum_count_word']]
            return data_5

          except:
            try:
              # Hanya res 1
              res_1 = model_2.wv.most_similar(text1)[0:5]
              df_res_1 = pd.DataFrame(res_1)
              df_result_6 = df_res_1.reset_index(drop=True)
              for item in df_result_6[0].unique():
                list_new.append(item)
              for i in range(len(data)):
                count_word_1.append(data['clean stopword'][i].count(list_new[0]))
                count_word_2.append(data['clean stopword'][i].count(list_new[1]))
                count_word_3.append(data['clean stopword'][i].count(list_new[2]))
                count_word_4.append(data['clean stopword'][i].count(list_new[3]))
                count_word_5.append(data['clean stopword'][i].count(list_new[4]))
              data['count_word_1'] = count_word_1
              data['count_word_2'] = count_word_2
              data['count_word_3'] = count_word_3
              data['count_word_4'] = count_word_4
              data['count_word_5'] = count_word_5
              data['sum_count_word'] = data.iloc[:,11:15].sum(axis=1)
              data_6 = data[data.sum_count_word != 0]
              data_6 = data_6.sort_values("sum_count_word", ascending=False)[['Nama','Tipe_1', 'Rating', 'Price', 'Daerah', 'sum_count_word']]
              return data_6

            except:
              print("Maaf Keyword Tidak ditemukan")

#FLOW 2
df_percent = pd.read_csv('df_percent.csv')
df_percent.set_index('Nama', inplace=True)
indices = pd.Series(df_percent.index)
cosdf = pd.read_csv('cos.csv',header=None)
cosine_similarities = cosdf.to_numpy()
def recommend(name, cosine_similarities = cosine_similarities):
    recommend_restaurant = []
    idx = indices[indices == name].index[0]
    score_series = pd.Series(cosine_similarities[idx]).sort_values(ascending=False)
    top30_indexes = list(score_series.iloc[0:31].index)
    for each in top30_indexes:
        recommend_restaurant.append(list(df_percent.index)[each])
    dat_for_filter = pd.DataFrame(columns=['Rating', 'Price', 'Daerah','Tipe_1', 'Tipe_2', 'Tipe_3'])
    for each in recommend_restaurant:
        dat_for_filter = dat_for_filter.append(pd.DataFrame(df_percent[['Rating', 'Price', 'Daerah','Tipe_1', 'Tipe_2', 'Tipe_3']][df_percent.index == each].sample()))
    dat_for_filter = dat_for_filter.drop_duplicates(subset=['Rating', 'Price', 'Daerah','Tipe_1', 'Tipe_2', 'Tipe_3'], keep=False)
    dat_for_filter = dat_for_filter.head(6)
    print('TOP %s TEMPAT MAKAN/RESTORAN YANG MEMILIKI REVIEW MIRIP %s : ' % (str(len(dat_for_filter)-1), name))
    return dat_for_filter[1:]

nama = (df['Nama'].sort_values()).reset_index(drop=True)
if opsi == 'Beranda':
    st.image(header2)
    # st.write('----')
    st.subheader('Klik untuk melihat partner MakanKuy!')
    st.write('Kami bekerja sama dengan 100+ tempat makan di Jakarta Selatan untuk memberikan rekomendasi terbaik untuk kepuasan Anda')
    # st.button('Lihat Partner Kami')
    if st.button('Lihat Partner Kami'):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            for i in range (0,35):
                st.write(i+1,'. ', nama[i])
        with col2:
            for i in range (35,70):
                st.write(i+1,'. ', nama[i])
        with col3:
            for i in range (70,105):
                st.write(i+1,'. ', nama[i])
        with col4:
            for i in range (105,120):
                st.write(i+1,'. ', nama[i])
            st.subheader('...dan masih banyak lagi!')
    st.write('-------')

    st.header('Jelajahi MakanKuy!')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(home1, use_column_width=True)
    with col2:
        st.image(home2, use_column_width=True)
    with col3:
        st.image(home3, use_column_width=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(home7, use_column_width=True)
    with col2:
        st.image(home8, use_column_width=True)
    with col3:
        st.image(home9, use_column_width=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(home4, use_column_width=True)
    with col2:
        st.image(home5, use_column_width=True)
    with col3:
        st.image(home6, use_column_width=True)
elif opsi == 'Rekomendasi berdasarkan budget':
    page2 = Image.open('page22.png')
    st.image(page2, use_column_width=True)
    # st.header('REKOMENDASI BERDASARKAN BUDGET')
    st.subheader('Silahkan isi sesuai dengan yang kamu mau!')
    text1=''
    text2=''
    text3=''

    with st.form('Cari'):
      col1, col2, col3 = st.columns(3)
      with col1:
          text1 = st.text_input('Kata Kunci 1')
      with col2:
          text2 = st.text_input('Kata Kunci 2')
      with col3:
          text3 = st.text_input('Kata Kunci 3')
      col1, col2, col3 = st.columns(3)
      with col1:
        daerah =  st.selectbox('Pilih Daerah : ', sorted(df_percent['Daerah'].unique()))
      with col2:
        harga = st.slider('Harga : ', 0, 1500000, value=100000, step=25000)
      with col3:
        tipe = st.selectbox('Pilih Tipe : ', sorted(df_percent['Tipe_1'].unique()))
      df1 = input_text(text1, text2, text3)
      if st.form_submit_button('Submit'):
        st.write('Rekomendasi berdasarkan : ', text1,', ', text2,', ', text3)
        st.write('Di daerah : ', daerah,'\n','Harga : ', harga,'\n','Kategori: ', tipe)
        df1 = df1[df1['Daerah'] == daerah]
        df1 = df1[df1['Tipe_1'] == tipe]
        df1 = df1[df1['Price'] <= harga] 
        # st.write(df1)
        img = df1['Nama'].to_list()
        # st.write(img[0])
        for i in range(len(img)):
          # st.subheader('1.')
          res1 = Image.open(df.loc[df['Nama']==str(img[i])]['Images'].values[0])
          col1, col2 = st.columns(2)
          with col1:
            st.image(res1)
          with col2:
            st.header(str(img[i]))
            st.subheader('Kategori : ' + str(df.loc[df['Nama']==str(img[i])]['Tipe_1'].values[0]))
            st.subheader('Rating : ' + str(df.loc[df['Nama']==str(img[i])]['Rating'].values[0])+' /5')
            st.subheader('Budget : Rp. ' + str(df.loc[df['Nama']==str(img[i])]['Price'].values[0]))
          st.write('-----')        
else:
    page3 = Image.open('page3.png')
    st.image(page3, use_column_width=True)
    # st.header('>>Kami berikan rekomendasi sesuai dengan referensi tempat makanmu')
    st.subheader('Silahkan isi sesuai dengan yang kamu mau!')
    # st.write('----')
    
    resto = st.selectbox('Pilih Tempat Makan Referensimu', nama)
    rt = ' /5'
    tes1=Image.open(df.loc[df['Nama']==resto]['Images'].values[0])
    tes1=tes1.resize((800,500))
    col1, col2 = st.columns((3,2))
    with col1:
        st.image(tes1)
    with col2:
        cont1 = st.container()
        cont1.header(df.loc[df['Nama']==resto]['Nama'].values[0])
        cont1.write('-----')
        cont1.subheader('DAERAH : ' +df.loc[df['Nama']==resto]['Daerah'].values[0])
        cont1.subheader('HARGA : '+ str(df.loc[df['Nama']==resto]['Price'].values[0]))
        cont1.subheader('KATEGORI : ')
        cont1.subheader('> '+ df.loc[df['Nama']==resto]['Tipe_1'].values[0] +', '+ df.loc[df['Nama']==resto]['Tipe_2'].values[0])
        cont1.subheader('RATING : ' + str(df.loc[df['Nama']==resto]['Rating'].values[0]) + str(' / 5'))
    st.write('-----')
    if st.button('Cari'):
        st.header('Berikut adalah rekomendasi sesuai referensimu : ')
        st.write('----')
        st.spinner('Memuat...')
        rcmnd = recommend(resto)
        # st.write(rcmnd)
        for i in range(len(rcmnd)):
          col1, col2 = st.columns((3,2))
          with col1:
            res1 = Image.open(df.loc[df['Nama']==rcmnd.index[i]]['Images'].values[0])
            st.image(res1, use_column_width=True,caption=rcmnd.index[i]+'\n'+rcmnd['Daerah'].values[0])
            st.write('-----')
          with col2:
            cont1 = st.container()
            cont1.header(df.loc[df['Nama']==rcmnd.index[i]]['Nama'].values[0])
            cont1.write('-----')
            cont1.subheader('DAERAH : ' +df.loc[df['Nama']==rcmnd.index[i]]['Daerah'].values[0])
            cont1.subheader('HARGA : '+ str(df.loc[df['Nama']==rcmnd.index[i]]['Price'].values[0]))
            cont1.subheader('KATEGORI : ')
            cont1.subheader('> '+ df.loc[df['Nama']==rcmnd.index[i]]['Tipe_1'].values[0] +', '+ df.loc[df['Nama']==rcmnd.index[i]]['Tipe_2'].values[0])
            cont1.subheader('RATING : ' + str(df.loc[df['Nama']==resto]['Rating'].values[0]) + str(' / 5'))
st.write('----')