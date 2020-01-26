import seaborn as sns,pandas as pd

html=pd.read_html('http://www.allelefrequencies.net/hla6006a_scr.asp?hla_locus=&hla_locus_type=Classical&hla_allele1=&hla_allele2=&hla_selection=&hla_pop_selection=&hla_population=1614&hla_country=&hla_dataset=&hla_region=&hla_ethnic=&hla_study=&hla_sample_size=&hla_sample_size_pattern=equal&hla_sample_year=&hla_sample_year_pattern=equal&hla_level=&hla_level_pattern=equal&hla_show=&hla_order=order_1&standard=a')
data=html[1]
freqs=data['Allele Frequency']
plot=sns.distplot(freqs)