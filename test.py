# success_data_lines = success_data[0].get("lines")
# count = 0
# element, xpath = find_dropdown_by_plceholder("Select Year")
# if element is not None:
#     if success_data[0].get("isYear") == 0:
#         # select No Year;
#         pass
#     elif success_data[0].get("isYear") == 1:
#         # select any year
#         pass
# for i in success_data_lines:
#     if i.get("linecharcount") != 0:
#         element, xpath = find_element_by_placeholder("line"+str(count+1))
#         count+=1
#         element.send_keys(gererateTest(int(i.linecharcount)))