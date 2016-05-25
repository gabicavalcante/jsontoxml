from xml.dom import minidom
from itertools import izip  # to transform list to a dict


def delete_tab(list):
    count = 0
    for res in list:
        try:
            if res.data == "\n\t\t\t":
                del list[count]
        except AttributeError:
            pass
        count += 1
    return list


def resources(data_xml):
    """
    :return: dic of resources and amount
    """
    data = minidom.parse(data_xml).getElementsByTagName("data")
    data = data[0].childNodes  # First data = contract + men + heading + budget
    contract = data[1]  # contract
    res_list = contract.childNodes  # List of amount+ resources
    res_list = delete_tab(res_list) # delete items related to tabulation
    # transform in dict
    # i = iter(resources)
    # r = dict(izip(i, i))
    r = {res_list[i].firstChild.data.strip(): res_list[i - 1].firstChild.data.strip() for i in
         range(1, len(res_list), 2)}
    return r


def print_resources(data_xml):
    res = resources(data_xml)

    for r in res:
        print (r + " : " + res[r])


def nb_resources(data_xml):
    """
    :return: number of resources
    """
    res = resources(data_xml)
    return len(res)


def resource_take(data_xml):
    """
    Take the resources from 'exploit' and 'transform'
    :param data_xml:
    :return:
    """
    # Update 'data' to 'actions
    data = minidom.parse(data_xml).getElementsByTagName("data")
    count = 0
    for d in data:
        a = delete_tab(d.childNodes)
        if d.childNodes[1].nodeName != "action" and d.childNodes[1].nodeName != "status":  # 1 with tabulation to take the element
            # try:
                # print d.childNodes[1].nodeName
            # except:
            del data[count]
        # print d.childNodes
        count += 1

    # update data to action of type 'exploit'
    """count = 0
    for d in data:
        if d.childNodes[1].firstChild.data.strip() == "exploit":
            print d.childNodes[3].childNodes[1].firstChild.data.strip()   #3 to parameters; 1 to resource ; firstChild = take name of resouce
            if data[count+1].childNodes[1].fistChild.data.strip() == "status": # action ok
                print "okkk"
        count +=1
    # update data to action of type and 'transform'"""

def analyzer_resource(data_xml):
    f = open("analyzer.log", 'a+')
    f.write("############# RESOURCES #############\n\n")

    f.write("Number of required resources in the contract : {0}".format(nb_resources(data_xml)))
    print_resources(data_xml)
    print resource_take(data_xml)
    f.close()


