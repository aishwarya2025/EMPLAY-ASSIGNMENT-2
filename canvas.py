#!/usr/bin/env python
# coding: utf-8

# In[6]:


from reportlab.lib.pagesizes import letter
def create_mock(file_name):
    c = canvas.Canvas(file_name, pagesize=letter)
    c.drawString(100, 750, "Bid Number: 12345")
    c.drawString(100, 730, "Title: Request for Proposal - IT Services")
    c.drawString(100, 710, "Due Date: December 20, 2024")
    c.drawString(100, 690, "Payment Terms: Net 30 days")
    c.drawString(100, 670, "Contact: info@example.com")
    c.drawString(100, 650, "Company: Example Corporation")
    c.save()

create_mock("sample_rfp.pdf")


# In[5]:


from reportlab.pdfgen import canvas


# In[3]:


pip install reportlab


# In[ ]:




