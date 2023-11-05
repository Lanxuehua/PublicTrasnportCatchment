# Travel-Catchment
Public transportation plays a crucial role in supporting and enhancing the functionality of city centres, the number of people can reach the city centre by public transit is one of the metrics evaluating the affordabity and accessibility of a city. 
This project used isochrone mapping to visualize the catchement area for public transport and driving respectively. An isochrone is defined as a line connecting equal travel time distances from any given location, which can tell us “How far can you travel from your starting point in a certain amount of time?" They are widely used in areas such as transportation planning, urban design, and location-based services. 

This project compare the 30 minutes catchments area through public transit and driving
- The catchment area assemed to arrive at the city/activity centres at 8:30 AM in 30 minutes at a working day
- Usual Residence in the catchment area indicates how many people can reach to the city/activity centres at 8:30 AM in 30 minutes at a working day
- 5 major cities (Sydeny, Melbourne, Brisbane, Adelaide, Perth) in Australia were compared
- 129 activity centres (defined in PLAN MELRBOURNE) in Metropolitan Melbourne were compared
- Area Multiplier is the multiple times of driving catchment area to public transit catchment area
- Population Multiplier is the multiple times of usual residence in driving catchment area to usual residence in public transit catchment area
- Number of usual residence was retrieved from ABS 2021 Census, place of usual residence based on Mesh Block
- Mesh Blocks are the smallest geographical area defined by the Australian Bureau of Statistics

### 5 Major Cities comparison
![Comparison 5 city](https://github.com/Lanxuehua/PublicTrasnportCatchment/assets/107735017/dc49309b-7115-4ef0-829c-56352a5e7922)

![image](https://github.com/Lanxuehua/PublicTrasnportCatchment/assets/107735017/1eebfd76-7fac-41d1-8e99-f7af4c91dbcc)

### Activity centres in Metropolitan Melbourne
Activity centres is one of the Melbourne 2030 strategies for urban growth. Melbourne 2030 emphasizes the important of activity centres to ensure the urban growth to be sustainable. It is the goal of Activity centres to reduce congestion, to provide Accessibility and social equity to residents. This is not the first time Melbourne implement activity centres plan. Melbourne had adopted the district centre policy in 1980s, but later it was abandoned because government made way for shopping centres. One of the criticisms is that the development of activity centres is not consistent with the construct of public transport. Without efficient public transport, 75% of trips to Melbourne activity centres were by car. Therefore, it is meaningful to assess the share of public transport for current Melbourne 2030 designated activity centres.
![image](https://github.com/Lanxuehua/PublicTrasnportCatchment/assets/107735017/50586236-b848-4e47-9904-d1a1e4c418cc)

### Methods
Mesh Block is the smallest geographical units in the Australian Statistical Geography Standard (ASGS), however, the boarder of isochrone map not exactly match with the boarder of mesh block, so percentage of usual resident were used.
![image](https://github.com/Lanxuehua/PublicTrasnportCatchment/assets/107735017/225d1299-84c2-4bc0-93e4-98b90e21bf3d)
