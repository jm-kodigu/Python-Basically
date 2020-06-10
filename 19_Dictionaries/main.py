phoned = {"beatriz":78320132,"luduvina":77329103,"aprilia":73939283,"lizania":70390298}

print(phoned)

# access
print(phoned["luduvina"])

# add items
phoned["alexandra"] = 79930182

print(phoned)

# modified
phoned["lizania"] = 89439200

print(phoned)

# dictionary inside dictionary
estudent_1 = {
				"ID":111,
				"name":"suzana suzan",
				"departament":"IT",
				"email":"suzazanan@gmail.com"	
			}

estudent_2 = {
				"ID":112,
				"name":"nuno t. kumis",
				"departament":"IT",
				"email":"nunokakatuaskumis@gmail.com"
			}

estudent = {
				111:estudent_1,
				112:estudent_2		
		}

print(estudent)