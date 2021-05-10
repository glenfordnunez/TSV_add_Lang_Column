import pandas as pd 

def main():
	
	# File Location of file imported from Fluentcards.com
	file_location = input("Where is the file B?" + " ")
	file_tsv = file_location
	#file_tsv = "/Users/glenfordnunez/Downloads/La Fiesta del Chivo (Spanish Edition)_basic_2_21_2021.tsv"
	df = pd.read_csv(file_tsv, sep='\t')


	def count_num_cols(df):
		# Sends number of columns into the Matrix
		return len(df.columns)

	count_num_cols(df)


	def create_new_lang_columnt(df, file_tsv, new_lang_abr):
		df[new_lang_abr] = new_lang_abr
		df.to_csv(file_tsv, index=False)

	
	# User Input for language 
	
	new_lang = input("What is the target language?\n" +"Should be two letter abbreviation?"+ " ")

	# Create new column with new language from user input 
	create_new_lang_columnt(df, file_location, new_lang)



	print(new_lang + " " + "Is the new target language!")


# indicates app
if __name__ == "__main__":
	main()