INVEST_ANALYSIS_PROMPT = """
Ti si ekspert Agile coach. Analiziraj sledecu user story prema sest INVEST kriterijuma.

User Story: {story}

Za svaki kriterijum dodeli ocenu od 0 do 10 i daj kratko obrazlozenje na srpskom jeziku.
Vrati ISKLJUCIVO validan JSON u ovom formatu (bez ikakvih dodatnih reci ili objasnjenja):
{{
  "scores": {{
    "Independent": <broj 0-10>,
    "Negotiable": <broj 0-10>,
    "Valuable": <broj 0-10>,
    "Estimable": <broj 0-10>,
    "Small": <broj 0-10>,
    "Testable": <broj 0-10>
  }},
  "explanations": {{
    "Independent": "<obrazlozenje na srpskom>",
    "Negotiable": "<obrazlozenje na srpskom>",
    "Valuable": "<obrazlozenje na srpskom>",
    "Estimable": "<obrazlozenje na srpskom>",
    "Small": "<obrazlozenje na srpskom>",
    "Testable": "<obrazlozenje na srpskom>"
  }},
  "recommendations": [
    "<konkretna preporuka 1>",
    "<konkretna preporuka 2>"
  ]
}}
"""