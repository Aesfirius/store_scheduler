

def combine_user_data(q_product_data, me):
    """
    res_groups =
        {
            <group_id>:
                {
                    '<products.product_date>':
                        {
                            products.product_loc.location_name:
                                {
                                    'location_desc': products.product_loc.location_desc,
                                    'location_coord': products.product_loc.location_coord,
                                    'location_photo': products.product_loc.location_photo,
                                    'products': [
                                        {
                                            'product_id': products.product_id,
                                            'product_name': products.product_name,
                                            'product_desc': products.product_desc,
                                            'product_amount': products.product_amount,
                                            'product_cost': products.product_cost,
                                            'product_photo': products.product_photo,
                                        },
                                    ]
                                }
                        }
                }
        }

    """
    res_groups = {}
    for n, pd in enumerate(q_product_data):
        for g in q_product_data[n].groups:
            if g == me:
                g = 'my list'
            if g not in res_groups:
                res_groups[g] = {}
            if pd.product_date is not None and pd.product_date not in res_groups[g]:
                res_groups[g][pd.product_date] = {}
            if pd.product_loc.location_name not in res_groups[g][pd.product_date]:
                res_groups[g][pd.product_date][pd.product_loc.location_name] = {}
            res_groups[g][pd.product_date][pd.product_loc.location_name]['location_desc'] = pd.product_loc.location_desc
            res_groups[g][pd.product_date][pd.product_loc.location_name][
                'location_coord'] = pd.product_loc.location_coord
            res_groups[g][pd.product_date][pd.product_loc.location_name][
                'location_photo'] = pd.product_loc.location_photo
            if 'products' not in res_groups[g][pd.product_date][pd.product_loc.location_name]:
                res_groups[g][pd.product_date][pd.product_loc.location_name]['products'] = []
            n_count = 0
            prds = res_groups[g][pd.product_date][pd.product_loc.location_name]['products']
            for p in prds:
                if 'product_id' not in p:
                    p['product_id'] = pd.product_id
                    p['product_name'] = pd.product_name
                    p['product_desc'] = pd.product_desc
                    p['product_amount'] = pd.product_amount
                    p['product_cost'] = pd.product_cost
                    p['product_photo'] = pd.product_photo
                elif 'product_id' in p and p['product_id'] != pd.product_id:
                    n_count += 1
            if n_count == len(prds):
                prds.append({
                    'product_id': pd.product_id,
                    'product_name': pd.product_name,
                    'product_desc': pd.product_desc,
                    'product_amount': pd.product_amount,
                    'product_cost': pd.product_cost,
                    'product_photo': pd.product_photo})
    return res_groups
