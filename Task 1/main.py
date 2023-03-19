from fastapi import FastAPI
import csv

app = FastAPI()

@app.get("/hello")
async def hello():
    # open .tsv file
    with open("sample.tsv") as file:
        # Passing the TSV file to 
        # reader() function
        # with tab delimiter
        # This function will
        # read data from file
        tsv_file = csv.reader(file, delimiter="\t")
        
        store = []

        # line = []
        # printing data line by line
        for line in tsv_file:
            # store.append(line)
            stripped_list = [s.strip() for s in line]
            stripped_list = list(filter(None, stripped_list))
            output_str = ", ".join(stripped_list)
            store.append(output_str)

        return store


# @app.get("/hello")
# async def hello():
#   return {"Welcome!"}