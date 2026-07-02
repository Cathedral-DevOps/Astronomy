from astroquery.simbad import Simbad

data_list = []

Simbad.add_some_output_messages = False
Simbad.add_votable_fields('plx')


def fetch_distance(star_name):
    print(f"-------Fetching distance for {star_name} from Simbad...-------")
    result_table = Simbad.query_object(star_name)
    if result_table is not None and len(result_table) > 0:
            parallax = result_table['plx_value'][0]  # Parallax in milliarcseconds
    
    if hasattr(parallax, 'mask') and result_table['plx_value'].mask[0]:
        print(f"Parallax data for {star_name} is not available.")
    elif parallax <= 0:
        print(f"Parallax data for {star_name} is invalid (non-positive).")
    else:
        distance_pc = 1000.0/parallax
        distance_ly = distance_pc * 3.26156
        print(f"Distance to {star_name}: {distance_pc:.2f} parsecs ({distance_ly:.2f} light-years)")
    return distance_pc, distance_ly
        
distance_pc, distance_ly = fetch_distance("Proxima Centauri")
distance_pc_2, distance_ly_2 = fetch_distance("Sirius")
distance_pc_3, distance_ly_3 = fetch_distance("HD 140283")
    
data_list.append(f"Proxima Centauri: {distance_ly:.2f} light-years ({distance_pc:.2f} parsecs)")
data_list.append(f"Sirius: {distance_ly_2:.2f} light-years ({distance_pc_2:.2f} parsecs)")
data_list.append(f"HD 140283: {distance_ly_3:.2f} light-years ({distance_pc_3:.2f} parsecs)")
print(data_list[0], data_list[1], data_list[2], sep="\n")