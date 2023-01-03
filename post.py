import os
import openai
import config

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Generate five potential hot topic ideas for home agent postings to help sell a home in the San Francisco Bay Area:\n\n1. How to Maximize Curb Appeal and Increase Home Value in the San Francisco Bay Area\n2. Exploring the Benefits of Living in the San Francisco Bay Area\n3. Tips for Staging a Home to Sell Quickly in the San Francisco Bay Area\n4. Utilizing Technology to Streamline Home Selling in the San Francisco Bay Area\n5. Understanding the Homebuying Process in the San Francisco Bay Area",
  temperature=0.77,
  max_tokens=521,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)