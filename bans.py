# Imports
from pandas import *
from numpy import *
import random

# List
ban_ids = []
ban_reasons = []
ban_list = []

# Make The Function
def create_dummy_bans(n_fields,csv_name):
  for i in range(n_fields):
    id = random.randint(9999999999,999999999999999999)
    bans = random.randint(1,100)
    ban_reaso = random.choice(['Innapropriate Content','Soliciting','Revealing Personal Information','Spam','Harrasment','Fraudulent Use','Threat to Public Safety','Cyberbullying','Promotion of Harmful Behaviors','Misinformation','Promoting Extremist Content','Violating Community Guidelines','Violating Copyright Law','Creating unsafe environments','Evading Bans','Impersonation','Evading Age Restrictions','Promoting Illegal Activities','Promoting offsite content'])
    ban_ids.append(id)
    ban_list.append(bans)
    ban_reasons.append(ban_reaso)

  x = {"User ID":ban_ids,"Bans":ban_list,"Ban Reasons": ban_reasons}
  x = DataFrame(x)
  x.to_csv(f'{csv_name}.csv',index=True)

# Running Code
# create_dummy_bans(1000,'bans')
