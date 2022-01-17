import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


motivation_by_state = pd.read_csv('Data\motivation_by_state.csv')
motivation_by_size = pd.read_csv('Data\motivation_by_size.csv')
motivation_by_industry = pd.read_csv('Data\motivation_by_industry.csv')

# print(motivation_by_state)
# motivation_by_state.columns
# motivation_by_state.info()
# print(motivation_by_size)
# motivation_by_size.columns
# motivation_by_size.info()
# print(motivation_by_industry)
# motivation_by_industry.columns
# motivation_by_industry.info()

motivation_by_size_highuse = motivation_by_size[motivation_by_size['NSFSZFI'] == 857]
total_size = motivation_by_size_highuse[motivation_by_size_highuse['MOTUSETECH'] == 'T1E04C99']['FIRMPDEMP'].item()
motivation_by_size_highuse = motivation_by_size_highuse[motivation_by_size_highuse.MOTUSETECH != 'T1E04C99']

for row in motivation_by_size_highuse['FIRMPDEMP']:
    motivation_by_size_highuse['NORM'] = ((motivation_by_size_highuse['FIRMPDEMP'] / total_size)*100).round(2)

fig1, ax1 = plt.subplots(figsize=(6,15))
ax1.barh(motivation_by_size_highuse['MOTUSETECH_LABEL'], motivation_by_size_highuse['NORM'])
ax1.set_yticklabels(labels=['To automate tasks performed by labor', 'To upgrade outdated processes or methods', 'To improve quality or reliability of processes or methods', 'To expand the range of goods or services', 'To adopt standards and accreditation', 'Some other reason'],fontsize=14)
ax1.set_title('Motivation to use Artificial Intelligence for firms with 10 employees or more', fontsize=16, fontweight='bold')
ax1.set_xlabel('Portion that selected each motivation (Percent)', fontsize=14, fontweight='bold')
ax1.bar_label(ax1.containers[0], fmt='%.2f', fontsize=14)


motivation_by_state_highuse = motivation_by_state[motivation_by_state['State'] == 'Delaware']
total_state = motivation_by_state_highuse[motivation_by_state_highuse['MOTUSETECH'] == 'T1E04C99']['FIRMPDEMP'].item()
motivation_by_state_highuse = motivation_by_state_highuse[motivation_by_state_highuse.MOTUSETECH != 'T1E04C99']

for row in motivation_by_state_highuse['FIRMPDEMP']:
    motivation_by_state_highuse['NORM'] = ((motivation_by_state_highuse['FIRMPDEMP'] / total_state)*100).round(2)

fig2, ax2 = plt.subplots(figsize=(6,15))
ax2.barh(motivation_by_state_highuse['MOTUSETECH_LABEL'], motivation_by_state_highuse['NORM'])
ax2.set_yticklabels(labels=['To automate tasks performed by labor', 'To upgrade outdated processes or methods', 'To improve quality or reliability of processes or methods', 'To expand the range of goods or services', 'To adopt standards and accreditation', 'Some other reason'],fontsize=14)
ax2.set_title('Motivation to use Artificial Intelligence for firms in Delaware', fontsize=16, fontweight='bold')
ax2.set_xlabel('Portion that selected each motivation (Percent)', fontsize=14, fontweight='bold')
ax2.bar_label(ax2.containers[0], fmt='%.2f', fontsize=14)

motivation_by_industry_highuse = motivation_by_industry[motivation_by_industry['NAICS2017_LABEL'] == 'Information']
total_industry = motivation_by_industry_highuse[motivation_by_industry_highuse['MOTUSETECH'] == 'T1E04C99']['FIRMPDEMP'].item()
motivation_by_industry_highuse = motivation_by_industry_highuse[motivation_by_industry_highuse.MOTUSETECH != 'T1E04C99']

for row in motivation_by_industry_highuse['FIRMPDEMP']:
    motivation_by_industry_highuse['NORM'] = ((motivation_by_industry_highuse['FIRMPDEMP'] / total_industry)*100).round(2)

fig3, ax3 = plt.subplots(figsize=(6,15))
ax3.barh(motivation_by_industry_highuse['MOTUSETECH_LABEL'], motivation_by_industry_highuse['NORM'])
ax3.set_yticklabels(labels=['To automate tasks performed by labor', 'To upgrade outdated processes or methods', 'To improve quality or reliability of processes or methods', 'To expand the range of goods or services', 'To adopt standards and accreditation', 'Some other reason'],fontsize=14)
ax3.set_title('Motivation to use Artificial Intelligence for firms in Information sector', fontsize=16, fontweight='bold')
ax3.set_xlabel('Portion that selected each motivation (Percent)', fontsize=14, fontweight='bold')
ax3.bar_label(ax3.containers[0], fmt='%.2f', fontsize=14)

plt.show()
