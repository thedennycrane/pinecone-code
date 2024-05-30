
# JSON cleaned cases
The Singopore cases were not in a standardized format, which made it difficult to organize the data. We tried our best to clean it using VAs (more information below), but the results were just subpar because of the variations and edge-cases. You can see the JSON cases under the json_cases folder. The "NoSections" folder are ones that didn't follow any paticular pattern.

# Explanation of Vector Database and Search Algo
Vector database was used for this application because the client wanted lawyers to find text based on meaning, rather than a text-to-text match. This "democratizes" the law search engine because lawyers don't need to know cases beforehand to find them...they can rely on a search engine to do the heavy-lifting.

For this paticular project, we used the standard ANN algorithm from Pinecone. All vector search algorithms are similar, but there may be slight differences across platforms. We opted to use Pinecone because it was a managed-vector database that abstracted the complexities and had a low price. We used the serverless option because during the time of this writing, Pinecone provided free credit.

# Chunking and Embeddings
During testing, we used a chunk size of 2K using the RecursiveCharacterSplitter. You are free to play with this number, but I would recommend keeping it 1-4K range for two reasons:
- Text is broken up by new-line characters. The average paragraph is in the 2-3K token range
- The text refers to itself. Keeping too small of a chunk size may cause some of the references to be lost because the chunking will cut the paragraph to be short.

Overlap token size was 300, because the sentences were related to each other (the case builds on itself as the text progresses)

For testing, we used the text-embedding-3-small from OpenAI because it was cost-effective and quick (the client wanted a quick and effective POC for this project). Considering the general nature of OpenAI embeddings, you are free to use any embeddings and will likely recieve similar performance (as long as it has law datasets in the training process)

# Meta-Data Considerations
We spent a significant amount of time experimenting on the best approach for the law search problem. The following were our learnings by the end of the project

1) Using raw html text for vector search is sufficient
We went back and forth multiple times on the best way to index the Vector Database. The best approach was to simply ingest the raw case text data. We attempted to partition the cases by section header...this was a non-scalable approach because the cases were not in a standardized format.

We even went as far as to hire VAs to clean the data...the data cleaning was mediocore. The problem was across the +8K cases, there were 20-50 different formats, with some not following any strict rule. This meant in the long-term, it would be tough to ingest cases in the standardized format.

Another key relealization during client's alpha testing was that the lawyers didn't look at the actual text. Rather, the clicked on the case that came up and viewed the full thing. The lawyers also mentioned that the cases returned were good and useful for their work. As a result, at the end, it was concluded the best approach is to ingest the HTML files raw without displaying the text retrieved to the user.

2) Sticking to simple filters
As mentioend above, one of the core problems with the Singaporean cases was that they were not in a standardized format. After having the VAs help us organize the text, the results were subpar. The data-cleaning was mediocore at best...and this was because of how many edge-cases and variations existed in the cases.  So at the end, the client believed that using simple filters (year, type of case, court type) were the best option for the MVP. All 3 filters can found by the name of the HTML file (and the url while scraping). The client also mentioned the laywers weren't paticularly concerneted about the filter we added (coram, lawyer name, law firm)



