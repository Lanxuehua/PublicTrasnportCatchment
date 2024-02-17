# Travel-Catchment
Public transportation plays a crucial role in supporting and enhancing the functionality of city centres, the number of people can reach the city centre by public transit is one of the metrics evaluating the affordabity and accessibility of a city. 
This project used isochrone mapping to visualize the catchement area for public transport and driving respectively. An isochrone is defined as a line connecting equal travel time distances from any given location, which can tell us “How far can you travel from your starting point in a certain amount of time?" They are widely used in areas such as transportation planning, urban design, and location-based services. 

This project compare the 30 minutes catchments area through public transit and driving
- The catchment area assemed to arrive at the city/activity centres at 8:30 AM in 30 minutes at a working day
- Usual Residence in the catchment area indicates how many people can reach to the city/activity centres at 8:30 AM in 30 minutes at a working day
- 129 activity centres (defined in PLAN MELRBOURNE) in Metropolitan Melbourne were compared
- Area Multiplier is the multiple times of driving catchment area to public transit catchment area
- Population Multiplier is the multiple times of usual residence in driving catchment area to usual residence in public transit catchment area
- Number of usual residence was retrieved from ABS 2021 Census, place of usual residence based on Mesh Block
- Mesh Blocks are the smallest geographical area defined by the Australian Bureau of Statistics

### Melbourne, Brisbane, and Adeleide
![Melbourne](https://github.com/Lanxuehua/PublicTrasnportCatchment/assets/107735017/96cdbf46-f302-40ba-8cbb-27677de34a0c)
![BrisbaneAAdeleide](https://github.com/Lanxuehua/PublicTrasnportCatchment/assets/107735017/751b543b-7b2e-4447-b218-7b049c08b8e0)

![image](https://github.com/Lanxuehua/PublicTrasnportCatchment/assets/107735017/22dc58d8-d7aa-46ff-b902-5e1aa354eff0)

### Activity centres in Metropolitan Melbourne
Activity centres is one of the Melbourne 2030 strategies for urban growth. Melbourne 2030 emphasizes the important of activity centres to ensure the urban growth to be sustainable. It is the goal of Activity centres to reduce congestion, to provide Accessibility and social equity to residents. This is not the first time Melbourne implement activity centres plan. Melbourne had adopted the district centre policy in 1980s, but later it was abandoned because government made way for shopping centres. One of the criticisms is that the development of activity centres is not consistent with the construct of public transport. Without efficient public transport, 75% of trips to Melbourne activity centres were by car. Therefore, it is meaningful to assess the share of public transport for current Melbourne 2030 designated activity centres.
![image](https://github.com/Lanxuehua/PublicTrasnportCatchment/assets/107735017/50586236-b848-4e47-9904-d1a1e4c418cc)

### Examples of Metropolitan Activity Centre
![BoxHillAFootscray](https://github.com/Lanxuehua/PublicTrasnportCatchment/assets/107735017/36b64ed8-ceae-4983-93bc-f9e94bc857db)

![Metropolitan Activity Centre](https://github.com/Lanxuehua/PublicTrasnportCatchment/assets/107735017/f77c28c2-889e-4d63-9e87-f3dc8844c568)

### Methods
Mesh Block is the smallest geographical units in the Australian Statistical Geography Standard (ASGS), however, the boarder of isochrone map not exactly match with the boarder of mesh block, so percentage of usual resident were used.
![image](https://github.com/Lanxuehua/PublicTrasnportCatchment/assets/107735017/225d1299-84c2-4bc0-93e4-98b90e21bf3d)

### About Catchment mapping
Travel Time were used in the project for isochrones mapping in major city central area, such as Sydeny Central and Melbourne Central.
For detailed analysis in Melbourne, Remix (https://www.remix.com/) was used for public transport mapping, because some of the bus routes are not recorded in Travel Time. 
Remix is a collaborative platform for transportation, moving the little Jane in the map, you can create the isochrone map with your desired attributes. 
The map per below shows 30 minutes public transport catchment area for each activities centers in Metropolitan Melbourne, using Remix and TravelTime respectively.
The differences revealed the facts that bus routes were missing, and this caused a huge differences in Doncaster area.
![image](https://github.com/Lanxuehua/PublicTrasnportCatchment/assets/107735017/3437ee5e-b707-4a8f-b75d-cad8c964150a)
