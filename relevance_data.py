previous_questions=['How has the use of wearable technology improved athlete performance?',
                   'What are the characteristics that define a particular music genre?',
                   'How can AI assist in analyzing large datasets in scientific research?',
                   'What are the potential benefits and risks of genetically modified organisms (GMOs) in food ',
                   'What are the most promising renewable energy sources for a sustainable future?',
                   'How can virtual reality enhance immersive learning experiences for students?',
                   'Can social media platforms be effective tools for organizing and mobilizing social movements?',
                   'What ethical considerations arise from the use of emerging medical technologies?',
                   'Have we found any promising candidates for hosting extraterrestrial life?',
                   'What conservation efforts are being made to protect biodiversity in the face of climate change?'
]

rel_enhanced_questions = []

q1 = "How has the use of wearable technology improved athlete performance across different sports when it comes to quantifiable metrics around endurance, motor control, injury prevention, and Return on Investment for professional training?"

q2 = "What are the key musical qualities like rhythm, tonality, instrumentation, melody, and lyrical themes that define and distinguish between genres as varied as jazz, hip-hop, rock, country, and electronic dance?"

q3 = "For complex interdisciplinary fields like systems biology, economics, and climate science that handle massive heterogeneous datasets, what techniques from deep learning, topological data analysis, and Bayesian inference show promise in augmenting human analysis and accelerating breakthrough discoveries?"

q4 = "Setting aside public perception debates, what do long-term empirical studies actually reveal around the potential health, agricultural efficiency, and nutritional benefits vs ecological and antibiotic resistance risks associated with genetically modifying the genomes of crops and livestock?"

q5 = "Accounting for capacity factors, storage requirements, transmission losses, construction costs, and scalability constraints, which renewable electricity sources such as onshore wind, rooftop solar, offshore wind, hydroelectric, geothermal, tidal, or wave energy can sustainably meet surging electricity demand by 2050 as global CO2 emissions must decrease by 45 percent relative to 2010 levels?"

q6 = "How can emerging technologies like omnidirectional treadmills, haptic gloves, scent replication, and VR telepresence provide uniquely heightened and customizable sensory experiences for K-12 or vocational education students to enhance engagement across learning modalities?"

q7 = "What data-driven insights around message framing, selective exposure, virality predictors, and network effects explain how digital activism movements can shape policy agendas by succeeding or failing to reach consensus around morally charged issues like climate justice or economic inequality?"

q8 = "As innovations from gene editing, neural implants, synthetic biology, and nanomedicine push ethical boundaries around consent, identity, augmentation, and hubris in unpredictable ways, what guiding principles and oversight guardrails ensure these emerging life science technologies improve quality of life rather than inadvertently cause harm?"

q9 = "Based on continuously improving observations of atmospheric biosignatures on exoplanets, potential subsurface liquid water on icy moons like Europa and Enceladus, and the longevity of extremophiles in harsh analog environments on Earth, what empirical criteria strengthen hopes around discovering basic or complex extraterrestrial life in our solar system or beyond in the coming decades?"

q10 = "Realizing that climate change has complex interrelated impacts across forests, coral reefs, the Arctic, antarctic, and every ecological niche, what data-driven policies, carbon removal efforts, ecosystem protections, assisted migrations, or emerging geoengineering strategies show promise in preventing irrecoverable biodiversity losses and ecological destabilization?"

rel_enhanced_questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]

rel_enhanced_questions_map = {}



question_pairs = {}
for i in range(len(previous_questions)):
    oq = previous_questions[i]
    eq = rel_enhanced_questions[i]

    question_pairs[oq] = eq

# print(question_pairs)






rel_questions_map = {}

# Populating the map with data
rel_questions_map[1] = {
    "How has the use of wearable technology improved athlete performance?": [
        "How does athlete work?",  # Less obvious as irrelevant (0)
        "How does wearable technology help athletes prevent injuries and monitor their overall health?",
        "What specific types of wearable technology are commonly used by athletes?",
        "Can you provide examples of professional athletes who have benefited from using wearable technology?",
        "What's the performance technology?",  # Less obvious as irrelevant (0)
        "How is the technology evolve in Earth?",  # Less obvious as irrelevant (0)
        "How does wearable technology track and analyze athlete performance?",
        "What are some key metrics that wearable technology can measure during training or competition?",
        "Are there any potential drawbacks or limitations to using wearable technology in sports?",
        "Can you discuss any notable studies or research conducted on the impact of wearable technology on athlete performance?"
    ]
}
ql1 = [0, 1, 1, 1, 0, 0, 1, 1, 1, 1]

rel_questions_map[2] = {
    "What are the characteristics that define a particular music genre?": [
        "How do music genres differ from one another in terms of sound and style?",
        "What's your favorite color?",  # Less obvious as irrelevant (0)
        "How do music genres evolve and change over time?",
        "How do cultural and historical factors influence the development of music genres?",
        "What are the key elements that contribute to the identity of a specific music genre?",
        "How does musician work?",  # Less obvious as irrelevant (0)
        "How do music genres influence fashion, lifestyle, and subcultures?",
        "How do music genres impact audience preferences and consumption patterns?",
        "Can music genres be blended or mixed together, and if so, what are the results?",
        "Are there any common themes or lyrical content associated with specific music performer?" # Less obvious as irrelevant (0),
    ]
}
ql2 = [0, 1, 1, 1, 0, 0, 1, 1, 1, 0]

rel_questions_map[3] = {
    "How can AI assist in analyzing large datasets in scientific research?": [
        "What specific techniques or algorithms does AI employ to analyze large scientific datasets?",
        "Can you provide examples of scientific research areas where AI has been successfully used for data analysis?",
        "What's the latest technology gadget on the market?",  # Irrelevant (0)
        "What are the advantages of using AI for data analysis compared to traditional statistical methods?",
        "Are there any limitations or potential biases that researchers should be aware of when using AI for dataset analysis?",
        "How does AI assist in identifying patterns, correlations, or anomalies in large scientific datasets?",
        "What are some of the computational requirements and resources needed to implement AI for data analysis?",
        "How many hours does AI assistant work?",  # Irrelevant (0)
        "Can you share your favorite recipe when you are doing research?",  # Irrelevant (0)
        "What ethical considerations should be taken into account when using AI in scientific research to analyze large datasets?"
    ]
}
ql3 = [1, 1, 0, 1, 1, 1, 1, 1, 0, 1]

rel_questions_map[4] = {
    "What are the potential benefits and risks of genetically modified organisms (GMOs) in food": [
        "How do genetically modified organisms (GMOs) provide potential benefits in terms of food production and agriculture?",
        "Can you provide specific examples of GMOs that have been developed for improved nutritional content or increased crop yield?",
        "What are the potential risks or concerns associated with consuming GMOs in food?",
        "How do GMOs impact biodiversity and the environment?",
        "How many steps do you typically make food?",  # Irrelevant (0)
        "Can GMOs help address global food security challenges, and if so, how?",
        "What scientific studies or research have been conducted to assess the safety of GMOs for human consumption?",
        "How do GMOs compare to traditional breeding methods in terms of their impact on food quality and safety?",
        "Are there any people associated with the use of GMOs in food production?",  # Irrelevant (0)
        "What's your preferred benefits and risks?",  # Irrelevant (0)
    ]
}

ql4 = [1, 1, 1, 1, 0, 1, 1, 1, 0, 0]


rel_questions_map[5] = {
    "What are the most promising renewable energy sources for a sustainable future?": [
        "What are the specific characteristics or advantages of each renewable energy source that make them promising for a sustainable future?",
        "Can you provide examples of countries or regions that have successfully implemented these renewable energy sources?",
        "How do these renewable energy sources compare in terms of their efficiency and reliability?",
        "Are there any challenges or limitations associated with the integration of these renewable energy sources into existing energy infrastructure?",
        "What advancements or innovations are being made to improve the scalability and affordability of these renewable distributed system?", # Irrelevant (0)
        "How do these renewable energy sources contribute to reducing greenhouse gas emissions and combating climate change?",
        "Are there any potential environmental impacts or concerns associated with the widespread adoption of these renewable energy sources?",
        "How do these renewable energy sources align with the goals outlined in international agreements such as the Paris Agreement?",
        "What are the energy source we use for concert?",   # Irrelevant (0)
        "What's your favorite energy source of the year?",  # Irrelevant (0)
    ]
}

ql5 = [1, 1, 1, 1, 0, 1, 1, 1, 0, 0]

rel_questions_map[6] = {
    "How can virtual reality enhance immersive learning experiences for students?": [
        "What are some specific examples of how virtual onsite interview is currently being used in educational settings?", # Irrelevant (0)
        "How does virtual reality enhance animal engagement and motivation ?", # Irrelevant (0)
        "Can you provide examples of subjects or topics where virtual reality has proven to be particularly effective in immersive learning experiences?",
        "What are the advantages of using virtual reality compared to traditional classroom teaching methods?",
        "Are there any limitations or challenges that educators should consider when implementing virtual reality in the classroom?",
        "How does virtual reality help students develop critical thinking and problem-solving skills?",
        "Are there any studies or research that demonstrate the impact of virtual reality on porn start learning outcomes?", # Irrelevant (0)
        "What types of virtual reality hardware and software are commonly used in educational settings?",
        "How does virtual reality facilitate experiential learning and the exploration of real-world scenarios?",
        "Are there any ethical considerations or guidelines that should be followed when using virtual reality in immersive learning experiences?"
    ]
}

ql6 = [0, 0, 1, 1, 1, 1, 0, 1, 1, 1]

rel_questions_map[7] = {
    "Can social media platforms be effective tools for organizing and mobilizing social movements?": [
        "What are some examples of social movements that have successfully utilized social media platforms for organizing and mobilization?",
        "How do social media platforms facilitate communication and information sharing among activists and supporters of social movements?",
        "What's your favorite type of dessert?",  # Irrelevant (0)
        "What are the advantages and disadvantages of using social media compared to traditional methods of organizing social movements?",
        "Are there any specific strategies or best practices for using social media effectively in mobilizing social movements?",
        "How do social media platforms help raise awareness and garner support for social movements?",
        "How many hours of sleep do you think is ideal?",  # Irrelevant (0)
        "Are there any risks or challenges associated with relying heavily on social media for organizing social movements?",
        "How do social media platforms enable global connections and solidarity among different social movements?",
        "What are some ethical considerations or concerns related to the use of FOX news"  # Irrelevant (0)
    ]
}

ql7 = [1, 1, 0, 1, 1, 1, 0, 1, 1, 0]


rel_questions_map[8] = {
    "What ethical considerations arise from the use of emerging medical technologies?": [
        "What's the population of a random city in a foreign country with emerging medical technologies?",  # Irrelevant (0)
        "What are the ethical considerations surrounding the affordability and cost-effectiveness of emerging talent?",  # Irrelevant (0)
        "Can you provide examples of potential ethical dilemmas that may arise from the use of these technologies?",
        "What are the implications of emerging medical technologies on healthcare accessibility and equity?",
        "Are there any concerns regarding the potential misuse or abuse of emerging medical technologies?",
        "How do these technologies impact the doctor-patient relationship and the autonomy of patients?",
        "What are the ethical considerations surrounding the affordability and cost-effectiveness of emerging medical technologies?",
        "Are there any legal or regulatory frameworks in place to address the ethical implications of these technologies?",
        "How do emerging sport technologies impact informed consent and athlete decision-making?", # Irrelevant (0)
        "Are there any potential long-term health or societal implications that need to be considered when adopting emerging medical technologies?"
    ]
}

ql8 = [0, 0, 1, 1, 1, 1, 1, 1, 0, 1]

rel_questions_map[9] = {
    "Have we found any promising candidates for hosting extraterrestrial life?": [
        "What criteria do scientists use to determine whether a apple is a promising candidate for hosting extraterrestrial life?", # Irrelevant (0)
        "Can you provide examples of celestial bodies within our solar system that are considered potential candidates for hosting extraterrestrial life?",
        "What are the key factors scientists look for when assessing the potential habitability of exoplanets outside our solar system?",
        "Are there any ongoing missions or telescopic observations focused on identifying promising candidates for extraterrestrial life?",
        "How do scientists search for signs of life or habitability on distant celestial bodies?",
        "What are the limitations or challenges in identifying and confirming potential candidates for hosting foreign students?", # Irrelevant (0)
        "Who won the last season of a reality TV show for extraterrestrial life?",  # Irrelevant (0)
        "Can you discuss any recent discoveries or findings that have shed light on potential candidates for hosting extraterrestrial life?",
        "How does the presence of liquid water or the availability of certain chemical compounds influence the likelihood of finding extraterrestrial life?",
        "What are the implications and potential societal impact if we were to discover and confirm the existence of extraterrestrial life on a candidate celestial body?"
    ]
}
ql9 = [0, 1, 1, 1, 1, 0, 0, 1, 1, 1]

rel_questions_map[10] = {
    "What conservation efforts are being made to protect biodiversity in the face of climate change?": [
        "Can you provide examples of specific conservation efforts or initiatives that are currently underway to protect biodiversity in the face of climate change?",
        "How does climate change specifically impact biodiversity and the delicate ecosystems that support it?",
        "Who won the last season of a climate change show?",  # Irrelevant (0)
        "What's the current exchange rate for protect biodiversity?",  # Irrelevant (0)
        "Can you discuss any notable studies or research that have been conducted on the impact of climate change on biodiversity?",
        "How does climate change affect the distribution and abundance of species?",
        "Are there any specific species or habitats that are particularly vulnerable to the combined impacts of climate change and biodiversity loss?",
        "How do conservation efforts consider the interconnectedness of ecosystems and the need for ecosystem-based approaches in addressing climate change impacts?",
        "What are the challenges or obstacles faced in implementing effective conservation measures for biodiversity in the context of climate change?",
        "What's your favorite type of conservation efforts?",  # Irrelevant (0)
    ]
}
ql10 = [1, 1, 0, 0, 1, 1, 1, 1, 1, 0]

rel_questions_relevance = {
    1: ql1,
    2: ql2,
    3: ql3,
    4: ql4,
    5: ql5,
    6: ql6,
    7: ql7,
    8: ql8,
    9: ql9,
    10: ql10,
}


"""
q1 = "How has the use of wearable technology improved athlete performance across different sports when it comes to quantifiable metrics around endurance, motor control, injury prevention, and Return on Investment for professional training?"
1. Can you provide specific examples of how wearable technology has improved endurance in different sports?
2. How do wearables help athletes enhance their motor control in sports that require precise movements?
3. Are there any studies or research that have quantified the impact of wearable technology on injury prevention in athletes?
4. Can you explain how wearables assist in optimizing recovery for athletes, and what metrics they track to determine the recovery process?
5. Have there been any notable cases where the return on investment for professional training significantly improved due to the use of wearable technology?
6. Are there any challenges or limitations in implementing wearable technology for athlete performance improvement that should be considered?
7. How do wearable technologies provide actionable insights and recommendations based on the data collected?
8. Are there any regulations or guidelines in place regarding the use of wearable technology in professional sports?
9. What are some potential risks or downsides associated with relying heavily on wearable technology for athlete performance improvement?
10. Are there any specific sports or activities where the use of wearable technology has not shown significant improvements in performance?

q2 = "What are the key musical qualities like rhythm, tonality, instrumentation, melody, and lyrical themes that define and distinguish between genres as varied as jazz, hip-hop, rock, country, and electronic dance?"
 1. Can you provide examples of specific jazz artists or songs that showcase the improvisational nature and complex harmonies you mentioned?
2. How has hip-hop evolved over time in terms of its rhythmic emphasis and lyrical themes?
3. Are there any notable rock subgenres that deviate from the typical characteristics you described?
4. Can you explain how country music has incorporated elements from other genres in recent years?
5. What are some popular subgenres within electronic dance music, and how do they differ in terms of instrumentation and beats?
6. Are there any specific artists or songs that have successfully blended multiple genres, creating a unique musical style?
7. How do the lyrical themes in rock music differ from those in hip-hop or country music?
8. Can you elaborate on the role of technology in shaping the sound and production of electronic dance music?
9. Are there any regional or cultural influences that have contributed to the distinct characteristics of these genres?
10. How have the advancements in music production and recording technology influenced the sound and evolution of these genres over time?

q3 = "For complex interdisciplinary fields like systems biology, economics, and climate science that handle massive heterogeneous datasets, what techniques from deep learning, topological data analysis, and Bayesian inference show promise in augmenting human analysis and accelerating breakthrough discoveries?"
1. Can you provide specific examples of how deep learning has been applied in systems biology, economics, and climate science?
2. How does topological data analysis work, and how can it be applied to analyze biological networks?
3. Are there any limitations or challenges associated with using deep learning in interdisciplinary fields like economics and climate science?
4. Can you elaborate on how Bayesian inference can be used to improve predictions and estimate uncertainties in climate science?
5. What are some potential ethical considerations or concerns when using deep learning in interdisciplinary fields?
6. How can the integration of deep learning, topological data analysis, and Bayesian inference enhance the accuracy and reliability of breakthrough discoveries in these fields?
7. Are there any notable success stories or breakthroughs that have been achieved using these techniques in systems biology, economics, or climate science?
8. What are the computational requirements and resources needed to implement deep learning, topological data analysis, and Bayesian inference in these fields?
9. Are there any ongoing research efforts or emerging trends in the application of these techniques to interdisciplinary fields?
10. Can you explain how the combination of these techniques can aid in decision-making processes related to systems biology, economics, and climate science?

q4 = "Setting aside public perception debates, what do long-term empirical studies actually reveal around the potential health, agricultural efficiency, and nutritional benefits vs ecological and antibiotic resistance risks associated with genetically modifying the genomes of crops and livestock?"
1. How do long-term empirical studies compare the nutritional benefits of genetically modified crops and livestock to their conventionally bred counterparts?
2. Are there any specific long-term studies that have examined the potential health risks associated with consuming genetically modified crops or livestock, such as allergenicity or toxicity?
3. Can you provide examples of long-term studies that have assessed the impact of genetically modified crops and livestock on soil health, ecosystem services, or overall ecological balance?
4. How do long-term empirical studies investigate the potential transfer of genetically modified traits to wild or non-target species, and what are the implications of such transfers?
5. Are there any long-term studies that have monitored the evolution of antibiotic resistance in livestock or the environment as a result of genetic modifications, and what are the key findings?
6. What are some of the economic considerations that long-term empirical studies take into account when assessing the agricultural efficiency and productivity of genetically modified crops and livestock?
7. How do long-term studies address the potential unintended consequences of genetic modifications, such as the emergence of secondary pests or changes in weed dynamics?
8. Can you provide examples of long-term studies that have compared the environmental impacts of genetically modified crops and livestock to alternative agricultural practices, such as organic farming?
9. How do long-term empirical studies account for the potential variability in outcomes based on different genetic modifications, crop or livestock species, or management practices?
10. What are the implications of long-term empirical studies on genetically modified crops and livestock for food security, sustainable agriculture, and the overall resilience of our food systems?

q5 = "Accounting for capacity factors, storage requirements, transmission losses, construction costs, and scalability constraints, which renewable electricity sources such as onshore wind, rooftop solar, offshore wind, hydroelectric, geothermal, tidal, or wave energy can sustainably meet surging electricity demand by 2050 as global CO2 emissions must decrease by 45 percent relative to 2010 levels?"
1. How do capacity factors differ among the various renewable electricity sources mentioned?
2. What are the typical storage requirements for each of the renewable sources?
3. Can you provide an estimate of transmission losses for each renewable source?
4. How do construction costs compare between onshore wind, offshore wind, and rooftop solar?
5. What are the scalability constraints associated with each renewable source?
6. Are there any specific regions where geothermal energy is more viable and scalable?
7. How do the environmental impacts of hydroelectric power compare to other renewable sources?
8. What advancements in technology are expected to improve the viability of offshore wind farms?
9. Are there any emerging technologies or innovations in tidal and wave energy that could address their scalability and capacity factors?
10. How does the intermittency of solar and wind power affect their ability to meet surging electricity demand?

q6 = "How can emerging technologies like omnidirectional treadmills, haptic gloves, scent replication, and VR telepresence provide uniquely heightened and customizable sensory experiences for K-12 or vocational education students to enhance engagement across learning modalities?"
1. Can you provide specific examples of how omnidirectional treadmills can be used in K-12 or vocational education to enhance sensory experiences?
2. How do haptic gloves simulate touch and how can they be utilized across different subjects in K-12 or vocational education?
3. What are some potential applications of scent replication technology in different learning modalities within K-12 or vocational education?
4. How does VR telepresence enable remote learning and collaboration opportunities for K-12 or vocational education students?
5. Are there any studies or research that demonstrate the impact of these technologies on student engagement and learning outcomes in K-12 or vocational education?
6. What are the potential cost implications of implementing these technologies in educational settings, and how can schools or institutions overcome financial barriers?
7. How can these technologies be integrated into existing curriculum frameworks to enhance student learning experiences?
8. Are there any safety considerations or guidelines that need to be addressed when using these technologies with K-12 or vocational education students?
9. What are some potential ways to ensure equitable access to these technologies for students from diverse socioeconomic backgrounds?
10. How can these technologies be leveraged to support students with special needs or different learning abilities in K-12 or vocational education?

q7 = "What data-driven insights around message framing, selective exposure, virality predictors, and network effects explain how digital activism movements can shape policy agendas by succeeding or failing to reach consensus around morally charged issues like climate justice or economic inequality?"
1. How does message framing differ between digital activism movements focused on climate justice and those addressing economic inequality?
2. Can you provide examples of digital activism campaigns that have failed to shape policy agendas on morally charged issues? What were the reasons for their failure?
3. What are some common biases or cognitive factors that influence selective exposure in the context of digital activism and shaping policy agendas?
4. Are there any specific content characteristics or emotional appeals that tend to make digital activism messages more likely to go viral?
5. How do network effects play a role in amplifying the impact of digital activism movements on policy agendas? Are there any network structures that are particularly conducive to success?
6. What are some ways that data-driven insights can help identify key stakeholders or decision-makers to target in order to shape policy agendas effectively?
7. Are there any patterns or correlations in the data that suggest certain strategies or approaches are more successful in achieving consensus on morally charged issues?
8. How do cultural and societal factors influence the effectiveness of digital activism movements in shaping policy agendas related to climate justice or economic inequality?
9. What are the potential long-term effects of successful digital activism movements on policy agendas? How sustainable are their impacts?
10. How can data-driven insights help digital activism movements navigate and respond to counter-messaging or opposition from stakeholders with conflicting interests?

q8 = "As innovations from gene editing, neural implants, synthetic biology, and nanomedicine push ethical boundaries around consent, identity, augmentation, and hubris in unpredictable ways, what guiding principles and oversight guardrails ensure these emerging life science technologies improve quality of life rather than inadvertently cause harm?"
1. What are some specific examples of ethical dilemmas that have emerged from the use of gene editing, neural implants, synthetic biology, or nanomedicine, and how have they been addressed?
2. How can the principle of beneficence be applied to ensure that emerging life science technologies prioritize improving quality of life and well-being?
3. Are there any existing regulatory frameworks or oversight mechanisms in place to guide the responsible development and use of these technologies?
4. How can transparency and accountability be ensured in the research, development, and deployment of these technologies to minimize potential harm?
5. What role can interdisciplinary ethics committees or advisory boards play in providing guidance and oversight for the ethical implications of these life science technologies?
6. How can public awareness and education about the ethical considerations of these technologies be enhanced to foster informed discussions and decision-making?
7. Are there any specific international conventions or agreements that address the ethical implications of emerging life science technologies, and how effective are they in practice?
8. What are the potential unintended consequences or risks associated with the use of these technologies, and how can they be proactively addressed?
9. How can marginalized communities or underrepresented groups be included in the ethical discourse and decision-making processes related to these technologies?
10. What are the responsibilities of researchers, developers, and policymakers in ensuring that these emerging life science technologies are used responsibly and in alignment with ethical principles?

q9 = "Based on continuously improving observations of atmospheric biosignatures on exoplanets, potential subsurface liquid water on icy moons like Europa and Enceladus, and the longevity of extremophiles in harsh analog environments on Earth, what empirical criteria strengthen hopes around discovering basic or complex extraterrestrial life in our solar system or beyond in the coming decades?"
1. What are some specific atmospheric biosignatures that scientists look for when searching for signs of life on exoplanets, and how do they contribute to the empirical criteria for potential extraterrestrial life?
2. How do the presence of subsurface liquid water on moons like Europa and Enceladus enhance the chances of discovering extraterrestrial life? What are the implications of such discoveries?
3. Can you provide examples of extremophiles on Earth and the analog environments in which they thrive? How does their resilience strengthen hopes for finding life in extreme conditions elsewhere?
4. What technological advancements or instruments are being developed or utilized to detect and analyze atmospheric biosignatures or signs of life on exoplanets or other celestial bodies?
5. How does the concept of habitable zones or Goldilocks zones in planetary systems contribute to the empirical criteria for potential extraterrestrial life?
6. Are there any ongoing missions or planned explorations that specifically target the search for extraterrestrial life within our solar system or beyond?
7. What role does astrobiology play in studying the origins and potential distribution of life in the universe, and how does it inform the empirical criteria for discovering extraterrestrial life?
8. How do scientists differentiate between the possibility of finding basic life forms versus complex life forms in their search for extraterrestrial life?
9. Are there any ethical considerations or guidelines that need to be taken into account when exploring the potential discovery of extraterrestrial life?
10. How does the discovery of potential extraterrestrial life, whether basic or complex, impact our understanding of the origin of life and the possibility of life's existence elsewhere in the universe?

q10 = "Realizing that climate change has complex interrelated impacts across forests, coral reefs, the Arctic, antarctic, and every ecological niche, what data-driven policies, carbon removal efforts, ecosystem protections, assisted migrations, or emerging geoengineering strategies show promise in preventing irrecoverable biodiversity losses and ecological destabilization?"
1. How can data-driven approaches help in identifying and prioritizing areas or species that are most vulnerable to climate change impacts, thus guiding targeted ecosystem protections?
2. What are some specific examples of successful carbon removal technologies or strategies that have been implemented and proven effective in mitigating biodiversity losses and ecological destabilization?
3. Are there any data-driven policies or initiatives that focus on promoting sustainable land management practices to mitigate the impacts of climate change on forests and other terrestrial ecosystems?
4. How can data analytics and modeling be leveraged to assess the potential effectiveness and unintended consequences of emerging geoengineering strategies for climate change mitigation?
5. What are some of the challenges associated with implementing assisted migrations as a strategy to protect biodiversity, and how can these challenges be addressed?
6. Can you provide examples of successful ecosystem restoration projects that have helped mitigate the impacts of climate change on biodiversity and ecosystems?
7. How do data-driven policies and strategies account for the interconnectedness and dependencies between different ecological niches and habitats?
8. What role can citizen science and public participation play in collecting data and informing decision-making processes related to biodiversity protection and climate change mitigation?
9. Are there any international frameworks or agreements in place that specifically address the protection of biodiversity in the face of climate change? How effective are they?
10. How can data-driven policies and strategies be integrated with local and indigenous knowledge systems to ensure culturally appropriate and context-specific approaches to preventing biodiversity losses and ecological destabilization?

"""
# Create a dictionary to store the questions

# Add the questions for question number 1 to the dictionary

rel_enhanced_questions_relevance = {

}

rel_enhanced_questions_map[1] = {
    "How has the use of wearable technology improved athlete performance across different sports when it comes to quantifiable metrics around endurance, motor control, injury prevention, and Return on Investment for professional training?" : [
        "Can you provide specific examples of how wearable technology has improved endurance in different sports?",
        "How do wearables help athletes enhance their motor control in sports that require precise movements?",
        "Are there any studies or research that have quantified the impact of wearable technology on injury prevention in athletes?",
        "Can you explain how wearables assist in optimizing recovery for athletes, and what metrics they track to determine the recovery process?",
        "Have there been any notable cases where the return on investment for professional training significantly improved due to the use of wearable technology?",
        "Can you share a fun fact about a random element on the wearable technology?",  # Irrelevant (0)
        "How do wearable guitar provide actionable insights and recommendations based on the data collected?", # Irrelevant (0)
        "Are there any regulations or guidelines in place regarding the use of wearable technology in professional sports?",
        "What are some potential risks or downsides associated with relying heavily on wearable technology for athlete performance improvement?",
        "What's your opinion on the best way to play basketball?",  # Irrelevant (0)
    ]
}
req1 = [1, 1, 1, 1, 1, 0, 0, 1, 1, 0]

rel_enhanced_questions_map[2] = {
    "What are the key musical qualities like rhythm, tonality, instrumentation, melody, and lyrical themes that define and distinguish between genres as varied as jazz, hip-hop, rock, country, and electronic dance?": [
        "Can you provide examples of specific jazz artists or songs that showcase the improvisational nature and complex harmonies you mentioned?",
        "How has hip-hop evolved over time in terms of its rhythmic emphasis and lyrical themes?",
        "Are there any notable move that deviate from the typical characteristics you described?", # Irrelevant (0)
        "What's your preferred brand of toothpaste?",  # Irrelevant (0)
        "What are some popular subgenres within dance , and how do they differ in terms of move and history?", # Irrelevant (0)
        "Are there any specific artists or songs that have successfully blended multiple genres, creating a unique musical style?",
        "How do the lyrical themes in rock music differ from those in hip-hop or country music?",
        "Can you elaborate on the role of technology in shaping the sound and production of electronic dance music?",
        "Are there any regional or cultural influences that have contributed to the distinct characteristics of these genres?",
        "How have the advancements in music production and recording technology influenced the sound and evolution of these genres over time?"
    ]
}

req2 = [1, 1, 0, 0, 0, 1, 1, 1, 1, 1]

rel_enhanced_questions_map[3] = {
    "For complex interdisciplinary fields like systems biology, economics, and climate science that handle massive heterogeneous datasets, what techniques from deep learning, topological data analysis, and Bayesian inference show promise in augmenting human analysis and accelerating breakthrough discoveries?": [
        "Can you provide specific examples of how deep learning has been applied in systems biology, economics, and climate science?",
        "How does topological data analysis work, and how can it be applied to analyze Africa?", # Irrelevant (0)
        "Are there any limitations or challenges associated with using deep learning in interdisciplinary fields like economics and climate science?",
        "What's your favorite season for outdoor activities?",  # Irrelevant (0)
        "Who is the winner of a beauty pageant you're not familiar with?",  # Irrelevant (0)
        "How can the integration of deep learning, topological data analysis, and Bayesian inference enhance the accuracy and reliability of breakthrough discoveries in these fields?",
        "Are there any notable success stories or breakthroughs that have been achieved using these techniques in systems biology, economics, or climate science?",
        "What are the computational requirements and resources needed to implement deep learning, topological data analysis, and Bayesian inference in these fields?",
        "Are there any ongoing research efforts or emerging trends in the application of these techniques to interdisciplinary fields?",
        "Can you explain how the combination of these techniques can aid in decision-making processes related to systems biology, economics, and climate science?"
    ]
}

req3 = [1, 1, 0, 1, 0, 0, 1, 1, 1, 1]

rel_enhanced_questions_map[4] = {
    "Based on continuously improving observations of atmospheric biosignatures on exoplanets, potential subsurface liquid water on icy moons like Europa and Enceladus, and the longevity of extremophiles in harsh analog environments on Earth, what empirical criteria strengthen hopes around discovering basic or complex extraterrestrial life in our solar system or beyond in the coming decades?": [
        "What are some specific atmospheric biosignatures that scientists look for when searching for signs of life on exoplanets, and how do they contribute to the empirical criteria for potential extraterrestrial life?",
        "How do the presence of subsurface liquid water on moons like Europa and Enceladus enhance the chances of discovering extraterrestrial life? What are the implications of such discoveries?",
        "What's your favorite type of pizza topping?",  # Irrelevant (0)
        "What technological advancements or instruments are being developed or utilized to detect and analyze atmospheric biosignatures or signs of life on exoplanets or other celestial bodies?",
        "How does the concept of habitable zones or Goldilocks zones in planetary systems contribute to the empirical criteria for potential extraterrestrial life?",
        "Are there any ongoing missions or planned explorations that specifically target the search for extraterrestrial life within our solar system or beyond?",
        "What role does astrobiology play in studying the origins and potential distribution of life in the universe, and how does it inform the empirical criteria for discovering extraterrestrial life?",
        "How do scientists differentiate between the possibility of finding basic life forms versus complex life forms in their search for extraterrestrial life?",
        "How many steps do you think is a good daily goal for walking?",  # Irrelevant (0)
        "Can you share a fun fact about a random element on the periodic table?",  # Irrelevant (0)
    ]
}

req4 = [1, 1, 0, 1, 1, 1, 1, 1, 0, 0]

rel_enhanced_questions_map[5] = {
    "Accounting for capacity factors, storage requirements, transmission losses, construction costs, and scalability constraints, which renewable electricity sources such as onshore wind, rooftop solar, offshore wind, hydroelectric, geothermal, tidal, or wave energy can sustainably meet surging electricity demand by 2050 as global CO2 emissions must decrease by 45 percent relative to 2010 levels?": [
        "How do capacity factors differ among the various renewable electricity sources mentioned?",
        "What are the typical storage requirements for each of the sources?", # Irrelevant (0)
        "Can you provide an estimate of transmission losses for each food consuming?", # Irrelevant (0)
        "How do construction costs compare between onshore wind, offshore wind, and rooftop solar?",
        "What are the scalability constraints associated with each renewable source?",
        "Are there any specific regions where geothermal energy is more viable and scalable?",
        "How do the environmental impacts of hydroelectric power compare to other renewable sources?",
        "What advancements in technology are expected to improve the viability of offshore wind farms?",
        "Are there any emerging technologies or innovations in VR that could address their scalability and capacity factors?", # Irrelevant (0)
        "How does the intermittency of solar and wind power affect their ability to meet surging electricity demand?"
    ]
}

req5 = [1, 0, 0, 1, 1, 1, 1, 1, 1, 0]

rel_enhanced_questions_map[6] = {
    "How can emerging technologies like omnidirectional treadmills, haptic gloves, scent replication, and VR telepresence provide uniquely heightened and customizable sensory experiences for K-12 or vocational education students to enhance engagement across learning modalities?": [
        "What's your favorite color of socks to wear?",  # Irrelevant (0)
        "Can you provide specific examples of how omnidirectional treadmills can be used in K-12 or vocational education to enhance sensory experiences?",
        "What are some potential applications of scent replication technology in different learning modalities within K-12 or vocational education?",
        "How does VR telepresence enable remote learning and collaboration opportunities for K-12 or vocational education students?",
        "Are there any studies or research that demonstrate the impact of these technologies on student engagement and learning outcomes in K-12 or vocational education?",
        "What are the potential cost implications of implementing these technologies in educational settings, and how can schools or institutions overcome financial barriers?",
        "How can these technologies be integrated into existing curriculum frameworks to enhance student learning experiences?",
        "Are there any safety considerations or guidelines that need to be addressed when using these arms?",  # Irrelevant (0)
        "Can you recommend a good podcast to listen to?",  # Irrelevant (0)
        "How can these technologies be leveraged to support students with special needs or different learning abilities in K-12 or vocational education?"
    ]
}

req6 = [0, 1, 1, 1, 1, 1, 1, 0, 0, 1]

rel_enhanced_questions_map[7] = {
    "What data-driven insights around message framing, selective exposure, virality predictors, and network effects explain how digital activism movements can shape policy agendas by succeeding or failing to reach consensus around morally charged issues like climate justice or economic inequality?": [
        "How does message framing differ between digital activism movements focused on climate justice and those addressing economic inequality?",
        "What's the exchange rate of a currency from a remote island?",  # Irrelevant (0)
        "What are some common biases or cognitive factors that influence selective exposure in the context of digital activism and shaping policy agendas?",
        "Are there any specific content characteristics or emotional appeals that tend to make digital activism messages more likely to go viral?",
        "How do network effects play a role in amplifying the impact of digital activism movements on policy agendas? Are there any network structures that are particularly conducive to success?",
        "What are some ways that data-driven insights can help identify key stakeholders or decision-makers to target in order to shape policy agendas effectively?",
        "Are there any patterns or correlations in the data that suggest certain strategies or approaches are more successful in achieving consensus on morally charged issues?",
        "What's your favorite type of breakfast cereal?",  # Irrelevant (0)
        "How many steps do you think is a good daily goal for walking?",  # Irrelevant (0)
        "How can data-driven insights help digital activism movements navigate and respond to counter-messaging or opposition from stakeholders with conflicting interests?"
    ]
}

req7 = [1, 0, 1, 1, 1, 1, 1, 0, 0, 1]

rel_enhanced_questions_map[8] = {
    "As innovations from gene editing, neural implants, synthetic biology, and nanomedicine push ethical boundaries around consent, identity, augmentation, and hubris in unpredictable ways, what guiding principles and oversight guardrails ensure these emerging life science technologies improve quality of life rather than inadvertently cause harm?": [
        "What are some specific examples of ethical dilemmas that have emerged from the use of gene editing, neural implants, synthetic biology, or nanomedicine, and how have they been addressed?",
        "How can the principle of beneficence be applied to ensure that emerging life science technologies prioritize improving quality of life and well-being?",
        "Are there any existing regulatory frameworks or oversight mechanisms in place to guide the responsible development and use of these technologies?",
        "How can transparency and accountability be ensured in the research, development, and deployment of these technologies to minimize potential harm?", # Irrelevant (0)
        "What role can interdisciplinary ethics committees or advisory boards play in providing guidance for student?", # Irrelevant (0)
        "How can public awareness and education about the ethical considerations of these technologies be enhanced to foster informed discussions and decision-making?",
        "Are there any specific international conventions or agreements that address the ethical implications of emerging life science technologies, and how effective are they in practice?",
        "What are the potential unintended consequences or risks associated with the use of these drugs, and how can they be proactively addressed?", # Irrelevant (0)
        "How can marginalized communities or underrepresented groups be included in the ethical discourse and decision-making processes related to these technologies?",
        "What are the responsibilities of researchers, developers, and policymakers in ensuring that these emerging life science technologies are used responsibly and in alignment with ethical principles?"
    ]
}

req8 = [1, 1, 1, 0, 0, 1, 1, 0, 1, 1]

rel_enhanced_questions_map[9] = {
    "Based on continuously improving observations of atmospheric biosignatures on exoplanets, potential subsurface liquid water on icy moons like Europa and Enceladus, and the longevity of extremophiles in harsh analog environments on Earth, what empirical criteria strengthen hopes around discovering basic or complex extraterrestrial life in our solar system or beyond in the coming decades?": [
        "What are some specific atmospheric biosignatures that scientists look for when searching for signs of life on exoplanets, and how do they contribute to the empirical criteria for potential extraterrestrial life?",
        "How do the presence of subsurface liquid water on moons like Europa and Enceladus enhance the chances of discovering earth? What are the implications of such discoveries?",
        "Can you provide examples of extremophiles on Earth and the analog environments in which they thrive? How does their resilience strengthen hopes for finding life in extreme conditions elsewhere?",
        "What technological advancements or instruments are being developed or utilized to detect and analyze atmospheric biosignatures or signs of life on exoplanets or other celestial bodies?",
        "How does the concept of habitable zones or Goldilocks zones in planetary systems contribute to the suns?", # Irrelevant (0)
        "Are there any ongoing missions or planned explorations that specifically target the search for extraterrestrial life within our solar system or beyond?",
        "What role does astrobiology play in studying the origins and potential distribution of life in the universe, and how does it inform the empirical criteria for discovering extraterrestrial life?",
        "What's your preferred brand of biosignatures?",  # Irrelevant (0)
        "Are there any ethical considerations or guidelines that need to be taken into account when exploring the potential discovery of basketball skill?", # Irrelevant (0)
        "How does the discovery of potential extraterrestrial life, whether basic or complex, impact our understanding of the origin of life and the possibility of life's existence elsewhere in the universe?"
    ]
}

req9 = [1, 1, 1, 0, 1, 1, 1, 0, 0, 1]

rel_enhanced_questions_map[10] = {
    "Realizing that climate change has complex interrelated impacts across forests, coral reefs, the Arctic, antarctic, and every ecological niche, what data-driven policies, carbon removal efforts, ecosystem protections, assisted migrations, or emerging geoengineering strategies show promise in preventing irrecoverable biodiversity losses and ecological destabilization?": [
        "How can data-driven approaches help in identifying and prioritizing areas or species that are most vulnerable to climate change impacts, thus guiding targeted ecosystem protections?",
        "What are some specific examples of successful carbon removal technologies or strategies that have been implemented and proven effective in mitigating biodiversity losses and ecological destabilization?",
        "Are there any data-driven policies or initiatives that focus on promoting sustainable land management practices to mitigate the impacts of climate change on forests and other terrestrial ecosystems?",
        "How can data analytics and modeling be leveraged to assess the potential effectiveness and unintended consequences of emerging geoengineering strategies for climate change mitigation?",
        "What are some of the challenges associated with implementing assisted migrations as a strategy to protect human, and how can these challenges be addressed?", # Irrelevant (0)
        "Can you provide examples of successful ecosystem restoration projects that have helped mitigate the impacts of climate change on biodiversity and ecosystems?",
        "What's your preferred mode of transportation in a city?",  # Irrelevant (0)
        "What role can citizen science and public participation play in collecting data and informing decision-making processes related to biodiversity protection and climate change mitigation?",
        "Are there any international frameworks or agreements in place that specifically address the protection of biodiversity in the face of climate change? How effective are they?",
        "How do fireflies produce light?",  # Irrelevant (0)
    ]
}

req10 = [1, 1, 1, 1, 0, 1, 0, 1, 1, 0]

rel_enhanced_questions_relevance = {
    1: req1,
    2: req2,
    3: req3,
    4: req4,
    5: req5,
    6: req6,
    7: req7,
    8: req8,
    9: req9,
    10: req10,
}

g_questions_map = {}
g_questions_map[1] = {
    "How has the use of wearable technology improved athlete performance?": {
        1: [
            "Which specific wearables are commonly used to monitor athlete performance?",
            "How do wearables track vital signs during athletic activities?",
            "Are there any drawbacks to relying solely on wearable data for athlete performance?",
            "What metrics do wearables capture to assess children endurance?", # Irrelevant (0)
            "Can you explain how wearables contribute to injury prevention in sports?"
        ],
        2: [
            "What specific types of wearable technology are commonly used by athletes?",
            "How does medical technology help athletes prevent injuries and monitor their overall health?", # Irrelevant (0)
            "What are some key metrics that wearable technology can measure during training or competition?",
            "Are there any potential drawbacks or limitations to using wearable technology in sports?",
            "Can you discuss any notable studies or research conducted on the impact of wearable technology on athlete performance?"
        ],
        3: ["Can you provide examples of sports disciplines where wearable technology has had a significant impact?",
            "What trends are emerging in the use of wearable technology in sports at the professional level?",
            "Are there any challenges in implementing wearable technology in team sports compared to individual sports?",
            "How does the use of wearable technology differ in sports with high-intensity training versus endurance-based sports?",
            "Can you discuss the role of wearable technology in enhancing sports analytics and strategy?"
        ]
    }
}
gql1 = [[1,1,1,0,1], [1,0,1,1,1], [1,1,1,1,1]]

g_questions_map[2] = {
    "What are the characteristics that define a particular music genre?": {
        1: [
            "Can you provide examples of specific music genres and their defining characteristics?",
            "How do musical elements like rhythm and instrumentation contribute to genre definition?",
            "Are there subgenres within larger music genres, and how do they differ in terms of characteristics?",
            "What role do lyrics play in defining the identity of a music genre?",
            "Can you explain how cultural factors influence the development of art genres?" # Irrelevant (0)
        ],
        2: [
            "How do specific instruments and their use define the sound of a music genre?",
            "Are there any notable artists or bands associated with pioneering certain music genres?",
            "What historical events or movements have influenced the evolution of music genres?",
            "Can you provide examples of songs that represent different paint genres effectively?", # Irrelevant (0)
            "How does technology impact the sound and production of music within genres?"
        ],
        3: [
            "What cultural and societal factors led to the emergence of hip-hop as a distinct music genre?",
            "How has the definition of 'rock' music evolved over the decades?",
            "Can you discuss the role of globalization in the fusion of music genres?",
            "What are some unconventional music genres that have emerged recently?",
            "How do music genres reflect the values and identity of different communities?"   # Irrelevant (0)
        ]
    }
}

gql2 = [[1,1,1,1,0], [1,1,1,0,1], [1,1,1,1,0]]

g_questions_map[3] = {
    "How can AI assist in analyzing large datasets in scientific research?": {
        1: [
            "What are the common challenges scientists face when dealing with large datasets in research?",
            "Can you explain the basic principles of how AI algorithms analyze data in scientific research?",
            "Are there any specific AI techniques that are particularly effective for data analysis in research?",
            "What are the potential benefits of using AI for data analysis in scientific studies?",
            "Can AI help in automating data preprocessing tasks for researchers?"
        ],
        2: [
            "How has AI been applied in real-world scientific research projects to analyze large datasets?",
            "What are some notable examples of AI-driven breakthroughs in scientific data analysis?",
            "Are there any limitations or ethical considerations when using AI in scientific research?",
            "Can you discuss the role of machine learning in pattern recognition and data interpretation for researchers?",
            "How do AI-driven data analytics compare to traditional statistical methods in research?"
        ],
        3: [
            "What interdisciplinary collaborations have emerged between AI experts and scientists in various domains?",
            "How can AI enhance data visualization and representation for research purposes?",
            "Are there AI-driven tools or platforms designed specifically for scientific data analysis?",
            "Can you provide insights into the future of AI and its impact on scientific discovery?",
            "What are the implications of using AI to analyze data for evidence-based policymaking in science?"
        ]
    }
}

gql3 = [[1,1,1,0,1], [1,0,1,1,1], [1,0,1,1,1]]

g_questions_map[4] = {
    "What are the potential benefits and risks of genetically modified organisms (GMOs) in food?": {
        1: [
            "What are GMOs, and how are they used in food production?",
            "What are the perceived benefits of GMOs in terms of food production and sustainability?",
            "What are some of the potential risks or concerns associated with consuming GMOs?",
            "Can you explain how GMOs may impact biodiversity and ecosystems?",
            "How do GMOs compare to traditional farming methods in terms of crop yield and resource use?"
        ],
        2: [
            "Are there specific examples of GMOs that have been developed to address nutritional deficiencies?",
            "What are the regulatory policies and safety assessments in place for GMOs in food?",
            "Can you discuss the public perception and controversies surrounding GMOs?",
            "Are there any studies or research findings that highlight the effects of GMO consumption on human health?",
            "How do GMOs contribute to global food security and addressing hunger?"
        ],
        3: [
            "What are the global trends in the cultivation and consumption of GMOs in food?",
            "How do different countries or regions regulate GMOs in their food supply chains?",
            "Can you provide insights into the ethical considerations surrounding GMOs in agriculture and food production?",
            "Are there any long-term environmental impacts of GMOs that researchers are studying?",
            "What is the future outlook for GMOs in terms of their role in sustainable agriculture and food security?"
        ]
    }
}

gql4 = [[1,1,1,0,1], [1,1,0,1,1], [1,1,1,1,0]]

g_questions_map[5] = {
    "What are the most promising renewable energy sources for a sustainable future?": {
        1: [
            "What are renewable energy sources, and why are they important for sustainability?",
            "What are some common examples of renewable energy sources?",
            "How do renewable energy sources differ from fossil fuels in terms of environmental impact?",
            "Can you explain the concept of energy efficiency in renewable technologies?",
            "What are the basic principles of harnessing energy from renewable sources?"
        ],
        2: [
            "Are there specific countries or regions that have made significant strides in adopting renewable energy?",
            "What are the economic implications of transitioning to renewable energy sources?",
            "Can you discuss the role of government policies and incentives in promoting renewable energy?",
            "Are there any emerging technologies or innovations in renewable energy production?",
            "How do renewable energy sources contribute to reducing greenhouse gas emissions?"
        ],
        3: [
            "What are the global trends in renewable energy adoption and investment?",
            "How do different renewable sources, such as solar, wind, and hydroelectric power, compare in terms of scalability?",
            "Can you provide insights into the challenges and barriers faced by the renewable energy sector?",
            "What is the outlook for renewable energy as a primary source of power in the coming decades?",
            "How does the integration of renewable energy sources impact grid stability and energy storage?"
        ]
    }
}

gql5 = [[1,1,1,0,1], [1,0,1,1,1], [1,1,1,1,0]]

g_questions_relevance = {
    1: [gql1[0], gql2[0], gql3[0], gql4[0], gql5[0]],
    2: [gql1[1], gql2[1], gql3[1], gql4[1], gql5[1]],
    3: [gql1[2], gql2[2], gql3[2], gql4[2], gql5[2]]
}