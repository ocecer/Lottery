# Import
import requests
import lxml.html as lh
import pandas as pd


class LotteryResult:
    # Get Lottery results
    def getResults(self, _urlStr, _rowNr, _nrOfWeeks=1):
        self.urlStr = _urlStr
        self.rowNr = _rowNr
        self.nrOfWeeks = _nrOfWeeks

        results = []

        # Connect to data source
        url = f"https://lotobayisi.com/{self.urlStr}-Butun-Veriler.aspx/"
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}
        response = requests.get(url, headers=headers)
        doc = lh.fromstring(response.content)

        # Parse data between <tr>..</tr> of HTML
        tr_elements = doc.xpath('//tr')

        # Check the length of the first row if the data correct
        # [len(tr) for tr in tr_elements[:self.rowNr]]

        # Find the header of the table
        col = []
        i = 0

        # Store header from the first row of data
        for t in tr_elements[0]:
            i += 1
            name = t.text_content()
            # print('%d:"%s"' % (i, name))
            col.append((name, []))

        # Stor the data from 2nd row
        for j in range(1, len(tr_elements)):
            # T is j'th row
            T = tr_elements[j]

            # If row is not of size 8, the //tr data is not from table
            if len(T) != 8:
                break

            # i is the index of column
            i = 0

            # Iterate through each element of the row
            for t in T.iterchildren():
                data = t.text_content()
                # Check if row is empty
                if i > 0:
                    # Convert any numerical value to integers
                    try:
                        data = int(data)
                    except:
                        pass
                # Append the data to the empty list of the i'th column
                col[i][1].append(data)
                # Increment i for the next column
                i += 1

        # Check the length of the df if the data correct
        # [len(C) for (title, C) in col]

        Dict = {title: column for (title, column) in col}
        df = pd.DataFrame(Dict)

        # Clean data
        cleanCols = ["Hft", "Tarih"]
        df[cleanCols] = df[cleanCols].replace(
            {'\r': '', '\n': '', ' ': ''}, regex=True)

        # df = df.drop('Tarih', axis=1)

        # Get the Results from the weeks
        results = df.head(self.nrOfWeeks)

        return results

    def six60(self, _nrOfWeeks=1):
        self.nrOfWeeks = _nrOfWeeks
        urlStr = "Super"
        rowNr = 8
        # Connect to data source
        # url = f"https://lotobayisi.com/{self.urlStr}-Butun-Veriler.aspx/"
        six60Results = self.getResults(urlStr, rowNr, self.nrOfWeeks)
        return six60Results

    def eight90(self, _nrOfWeeks=1):
        self.nrOfWeeks = _nrOfWeeks
        urlStr = "Sayisal"
        rowNr = 10
        # Connect to data source
        # url = f"https://lotobayisi.com/{self.urlStr}-Butun-Veriler.aspx/"
        eight90Results = self.getResults(urlStr, rowNr, self.nrOfWeeks)
        return eight90Results


# sonuc = LotteryResult().six60()
# print("------------------")
# print(sonuc)
# print("------------------")
