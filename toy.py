import request_lib as lib

# get token and ad id
ACCESSTOKEN, ADID = lib.get_credential()

# build id dictionary
id_dictionary = lib.build_id_dictionary("categories.csv")
group_ids = list(id_dictionary.keys())
print("\n----User Group IDs:\n")
print(group_ids)
raw_input("Press Enter to see country codes...")

# build country dictionary
country_dictionary = lib.build_country_dictionary("country_codes.csv")
country_codes = list(country_dictionary.keys())
print("\n----2 Letter Country Codes:\n")
print(country_codes)
raw_input("Press Enter to see parameters...")

# for each job id
for i in range(0, 1):
    GROUP_ID = group_ids[i]
    ID_TYPE = id_dictionary[GROUP_ID]

    # for each country code make request
    for j in range(0, 1):
        COUNTRY = country_codes[j]

        # build query params
        params = lib.build_params(COUNTRY, GROUP_ID, ID_TYPE);
        print("\n----Constructed Paramters:\n")
        for param in params:
            print(param)
        raw_input("Press Enter to see urls...")

        # build urls with given params
        url_list = lib.build_url(params, ACCESSTOKEN, ADID)
        print("\n----Constructed URLs:\n")
        for url in url_list:
            print(url)

print("\nHope that helps you understand the queries!")