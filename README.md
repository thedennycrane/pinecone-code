# Purpose of Project
Client wanted to build a quick MVP of a law search engine that allows lawyers to easily find cases. The current search engine (lawnet) had limited customizability, UI-friendliness, and UX. The main purpose of this project is to validate the core search logic (Vector Search)


# Explanation of Vector Database and Search Algo
Vector database was used for this application because the client wanted lawyers to find text based on meaning, rather than a text-to-text match. This "democratizes" the law search engine because lawyers don't need to know cases beforehand to find them...they can rely on key-terms and search algorithm to do the heavy-lifting.

For this paticular project, we used the standard ANN algorithm from Pinecone. We opted to use Pinecone because it was a managed-vector database that abstracted the complexities and had a low price. We used the serverless option because during the time of writing, Pinecone provided free credits. All vector search algorithms are very similar, so you shoudn't notice a performance difference if you switched platforms.

The main thing is that the users were impressed and happy with the results that the Vector Search gave them.

# JSON cleaned cases
The scraped cases from the Singapore Government website are in cases_html. One of the most difficult part of this project was that the cases were not in a standardized format. This made it impossible to clean the data. We tried our best to clean it using VAs, but the results were just subpar because of sheer amount of variations and edge-cases. You can see the JSON cases under the json_cases folder. The "NoSections" folder are ones that didn't follow any paticular pattern.

# Chunking and Embeddings
During testing, we used a chunk size of 2K using the RecursiveCharacterSplitter. You are free to play with this number, but I would recommend keeping it 1-4K range for two reasons:
- Text is broken up by new-line characters. The average paragraph is in the 2-3K token range
- The text refers to itself. Keeping too small of a chunk size may cause some of the references to be lost because the chunking will cut the paragraph to be short.

Overlap token size was 300, because the sentences were related to each other (the case builds on itself as the text progresses). Note that during this project, because the client wanted better readability, the text is already chunked based on the section-title and section-text.

For testing, we used the text-embedding-3-small from OpenAI because it was cost-effective and quick (the client wanted a quick and effective POC for this project). Considering the general application of OpenAI embeddings, you are free to use any embeddings and will likely recieve similar performance (as long as it has law datasets in the training process).

# Meta-Data Considerations
We spent a significant amount of time experimenting on the best approach for the law search problem. The following were our learnings by the end of the project

### Using raw html text for vector search is sufficient

We went back and forth multiple times on the best way to index the Vector Database. The best approach was to simply ingest the raw case text data.

We attempted to partition the cases by section header...this didn't work because the data wasn't in a standard format. After hiring VAs to clean the data...the results were mediocore. The problem was across the +8K cases, there were 20-50 different formats, with some not following any strict rule. This meant in the long-term, it would be tough to ingest cases in the standardized format (not scalable)

Another key relealization during client's alpha testing was that the lawyers didn't look at the actual text. Rather, the clicked on the case that came up and viewed the full thing. The lawyers also mentioned that the cases returned were good and useful for their work. As a result, at the end, it was concluded the best approach is to ingest the HTML files raw without displaying the text retrieved to the user.

### Sticking to simple filters
As mentioned above, one of the core problems with the Singaporean cases was that they were not in a standardized format. After having the VAs help us clean the text, the results were subpar. So at the end, the client believed that using simple filters (year, type of case, court type) were the best option for the MVP. All 3 filters can found by the name of the HTML file (and the url while scraping). Some of the other filters that seemed important were validated to be unimportant during user testing (coram name, lawyer name, law firm)



