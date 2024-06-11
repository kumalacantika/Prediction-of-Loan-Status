import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


st.write('### Nama : Kumala Cantika Ainun Maya')
st.write('### Batch : SBY-004')
st.write('### Objective : ')
st.write('##### Pada bagian ini berisikan EDA data informasi nasabah dengan kelayakan diberikan pinjaman')
st.markdown('---')


    # Load dataset
    st.write('### Data Loan Status Nasabah')
    df = pd.read_csv('train.csv')
    st.dataframe(df)


    st.markdown('---')
    st.title('Exploratory Data Analysis(EDA) Data Layak Pinjam Nasabah')

    # Plot Target
    st.write('### Pie Chart Loan Status Nasabah')
    fig,ax1 = plt.subplots(figsize=(5,5))
    df['Loan_Status'].value_counts().plot(kind='pie',labels=['yes', 'no'],
                                                        autopct='%.2f%%',ax=ax1, colors=['lime','red'])
    st.pyplot(fig)
    st.write('''
    Pie chart tersebut merupakan perbandingan antara target yang layak dan tidak layak mendapatkan pinjaman, 
    yang mana hanya sekitar **68.73%** nasabah yang layak untuk mendapatkan pinjaman.
    ''')
    st.markdown('---')

    # Plot ApplicantIncome
    st.write('### Histogram dan Box Plot Pendapatan Nasabah')
    fig = plt.figure(figsize=(15, 6))
    # Histogram
    plt.subplot(1, 2, 1)
    sns.histplot(data=df['ApplicantIncome'], palette='Set1', color='cyan')
    plt.title('Histogram Pendapatan Nasabah')
    plt.xlabel('Pendapatan')
    plt.ylabel('Total')
    # Boxplot
    plt.subplot(1, 2, 2)
    sns.boxplot(y=df['ApplicantIncome'], color='cyan')
    plt.title('Boxplot Pendapatan')
    plt.xlabel('Pendapatan')
    st.pyplot(fig)
    st.write('''
    Berdasarkan visualisasi histogram dan boxplot menunjukkan bahwa:
    
        - Persebaran data pendapatan nasabah mayoritas ada pada rentang lebih dari 0 dan kurang dari sama dengan 10000
        - Terdapat banyak outlier yang terlihat dalam visualisasi boxplot
        - Persebaran data cenderung miring kanan/ skew, sehingga mungkin diperlukan cek skewness pada fitur ini
    ''')
    st.markdown('---')

    # Plot Coapllicantincome
    st.write('### Histogram dan Box Plot Pendapatan Sampingan Nasabah')
    fig = plt.figure(figsize=(15, 6))
    # Scatterplot
    plt.subplot(1, 2, 1)
    sns.scatterplot(data=df['CoapplicantIncome'], palette='Set1', color='red')
    plt.title('Histogram Pendapatan Sampingan Nasabah')
    plt.xlabel('Pendapatan Sampingan')
    plt.ylabel('Total')
    # Boxplot
    plt.subplot(1, 2, 2)
    sns.boxplot(y=df['CoapplicantIncome'], color='red')
    plt.title('Boxplot Pendapatan Sampingan')
    plt.xlabel('Pendapatan Sampingan')
    st.pyplot(fig)
    st.write('''
    Berdasarkan visualisasi histogram dan boxplot menunjukkan bahwa:

        - Persebaran data pendapatan nasabah mayoritas ada pada rentang 0 hingga kurang dari 10000
        - Terdapat banyak outlier yang terlihat dalam visualisasi boxplot
        - Persebaran data cenderung miring kanan/ skew, sehingga mungkin diperlukan cek skewness pada fitur ini
        - Jika dibandingkan dengan `ApplicantIncome`, pendapatan sampingan yang dimiliki oleh nasabah jauh lebih sedikit dibandingkan pendapatan utama
            ''')
    st.markdown('---')


    # Plot Loan Amount
    st.write('### Histogram dan Box Plot Pinjaman Nasabah')
    fig = plt.figure(figsize=(15, 6))
    # Distogram
    plt.subplot(1, 2, 1)
    sns.distplot(df['LoanAmount'], color='grey')
    plt.title('Histogram Besar Pinjaman')
    plt.xlabel('Pinjaman')
    plt.ylabel('Total')
    # Boxplot
    plt.subplot(1, 2, 2)
    sns.boxplot(y=df['LoanAmount'], color='grey')
    plt.title('Boxplot Besar Pinjaman')
    plt.xlabel('Pinjaman')
    st.pyplot(fig)
    st.write('''
    Berdasarkan visualisasi histogram dan boxplot menunjukkan bahwa:
    
        - Persebaran data mayoritas pinjaman yang diajukan oleh nasabah adalah mulai rentang lebih dari sama dengan 100 hingga kurang dari 200
        - Terdapat banyak outlier yang terlihat dalam visualisasi boxplot
        - Persebaran data cenderung miring kanan/ skew, sehingga mungkin diperlukan cek skewness juga pada fitur ini
    ''')
    st.markdown('---')

    # EDA catgoeical
    st.write('### Pie Chart Informasi Status Nasabah')
    fig = plt.figure(figsize = (20,10))

    # Fitur Gender
    plt.subplot(1,4,1) 
    plt.pie(df['Gender'].value_counts(), labels=['Male', 'Female'], autopct='%1.0f%%',colors=['orange','grey'])
    plt.title('Perbandingan Jenis Kelamin Nasabah')
    # Fitur Married  
    plt.subplot(1,4,2) 
    plt.pie(df['Married'].value_counts(), labels=['Yes', 'No'], autopct='%1.0f%%',colors=['orange','grey'])
    plt.title('Perbandingan Status Nasabah')
    # Fitur Self Employed  
    plt.subplot(1,4,3) 
    plt.pie(df['Self_Employed'].value_counts(), labels=['No', 'Yes'], autopct='%1.0f%%',colors=['orange','grey'])
    plt.title('Perbandingan Status Pekerjaan Nasabah')
    # Fitur Credit_History
    plt.subplot(1,4,4) 
    plt.pie(df['Credit_History'].value_counts(), labels=['Yes', 'No'], autopct='%1.0f%%',colors=['orange','grey'])
    plt.title('Perbandingan Rekam Pinjaman Nasabah')
    st.pyplot(fig)
    st.write('''
    Hasil visualisasi 4 fitur categorical `Gender`, `Married`, `Self_Employed`, dan `Credit_History` diperoleh beberapa hal berikut:

        - Sekitar 81% nasabah berjenis kelamin pria
        - Sekitar 65% nasabah sudah berkeluarga
        - Sekitar 86% nasabah tidak bekerja secara mandiri (bekerja kepada badan atau orang lain, sehingga berkemungkinan memiliki pendapatan yang tetap)
        - Sekitar 84% nasabah sudah pernah melakukan pinjaman sebelumnya 
    ''')
    st.markdown('---')

    # Plot bar perbadingan status Dependents
    st.write('### Jumlah Tanggungan Nasabah')
    fig,ax1 = plt.subplots(figsize=(5,5))
    df['Dependents'].value_counts().sort_index().plot(kind='bar', rot=0, color='navy')
    plt.xlabel('Tanggungan (orang)')
    plt.ylabel('Jumlah')
    st.pyplot(fig)
    st.write('''
    Berdasarkan visualisasi bar perbandingan jumlah tanggungan yang dimiliki nasabah diketahui bahwa:

        - Sebagian besar nasabah tidak memiliki tanggungan pembiayaan
    ''')
    st.markdown('---')

    # Plot Loan Amount Term
    st.write('### Scatter Persebaran Rentang Waktu Peminjaman')
    fig = plt.figure(figsize=(10, 4))
    sns.scatterplot(data=df['Loan_Amount_Term'], palette='Set1', color='pink')
    plt.xlabel('Waktu(hari)')
    plt.ylabel('Jumlah')
    st.pyplot(fig)
    st.write('''
    Berdasarkan visualisasi histagram diatas menunjukkan bahwa:

        - Rentang waktu peminjaman paling sering adalah dalam rentang 300 hingga 400 atau lebih tepatnya pada **360 hari** 
        - Dalam rentang waktu tersebut dapat juga berarti nasabah sebagian besar memiliki rentang waktu peminjaman selama 1 tahun lamanya.
    ''')
    st.markdown('---')


if __name__ == '__main__':
    run()
