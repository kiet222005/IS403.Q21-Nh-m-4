import pandas as pd

df = pd.read_csv('data_new/itd_new.csv')

# Lay cac hang co EPS khac nhau (drop_duplicates)
df_q = df[['date', 'EPS 4 quy']].drop_duplicates(subset=['EPS 4 quy'], keep='last')

print(f'Tong so diem EPS duy nhat: {len(df_q)}')
print()
print('10 diem cuoi:')
print(df_q.tail(10).to_string())
print()

eps_cur  = df_q['EPS 4 quy'].iloc[-1]
eps_last = df_q['EPS 4 quy'].iloc[-5]

print('--- Diem dung cho EPS Growth ---')
print(f'eps_cur  (iloc[-1]): date={df_q["date"].iloc[-1]}, EPS={eps_cur}')
print(f'eps_last (iloc[-5]): date={df_q["date"].iloc[-5]}, EPS={eps_last}')

growth = (eps_cur - eps_last) / abs(eps_last) * 100 if eps_last != 0 else 0
print(f'EPS Growth = ({eps_cur} - {eps_last}) / {abs(eps_last)} = {growth:.2f}%')
