def nan_replace_df(tabel):
    #pt fiecare col cu val lipsa:
    #numerica -> media, text -> val cea mai frecv
    tabel.fillna(tabel.mean(numeric_only=True), inplace=True)
