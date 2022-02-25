import json


def get_category(categorys):
    sub_str = ''
    for category in categorys:
        id = category['CategoryId']
        code = category['CategoryCode']
        name = category['CategoryName']
        if name == '全部':
            continue
        grade = category['Grade']
        picture_url = category['PictureUrl']
        parent_id = category['PriorId']

        sub_str += "('%s', '%s', '%s', %s, '%s', '%s'),\n" % (id, code, name, grade, picture_url, parent_id )
        if category['Childs']:
            sub_str += get_category(category['Childs'])
    return sub_str

        # yield {
        #     'id': id,
        #     'code': code,
        #     'name': name,
        #     'grade': grade,
        #     'picture_url': picture_url,
        #     'parent_id': parent_id,
        # }


with open('category.json') as f:
    category_dict = json.load(f)
    all_category = category_dict['Data']['CategoryList']
    sql = 'insert into t_category(id,code,name,grade,picture_url,parent_id) values '
    sub_str = get_category(all_category)

    with open('category.sql', 'w', encoding='utf-8') as sql_f:
        sql_f.write(sql + '\n' + sub_str)

