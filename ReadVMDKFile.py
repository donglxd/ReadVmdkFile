#coding=utf8
import os
from graphviz import Digraph
import doctest as dc

def getVMDKinfo(filePath):
    with open(filePath,'r',encoding ="utf-8",errors="ignore") as f:
        count = 0
        CurrentVMDK = os.path.split(filePath)[1]
        CID = ""
        ParentVMDK = ""
        parentCID = ""
        while 1:
            res = f.readline()
            print(res)
            count += 1
            if count > 10:
                print("---------------read_vmdk_end----------------")
                if CurrentVMDK =="":
                    print("Current VMDK IS " + 'Null')
                else:
                    print("Current VMDK IS " + '"' + CurrentVMDK + '"')
                if CID =="":
                    print("CID IS " + 'Null')
                else:
                    print("CID IS " + CID)
                if ParentVMDK =="":
                    print("ParentVMDK IS " + 'Null')
                else:
                    print("ParentVMDK IS " + '"' + ParentVMDK + '"')
                if ParentCID =="":
                    print("parentCID IS " + 'Null')
                else:
                    print("parentCID IS " + ParentCID)
                arr = [CurrentVMDK,CID,ParentVMDK,ParentCID] 
                break
            elif res[:3] == "CID":
                CID = res[4:-1]
            elif res[:9] == "parentCID":
                ParentCID = res[10:-1]
            elif res[:18] == "parentFileNameHint":
                ParentVMDK = res[20:-2]
        return arr

# getVMDKinfo(r'C:\Users\Donglxd\Desktop\测试\Windows 7-000001.vmdk')

def drawVMDKinfo(path):
    g = os.walk(path)
    #g = os.walk(r'C:\Users\Donglxd\Desktop\测试')

    #dot = grap.Graph(format='png')
    dot = Digraph('G', format='png')
    nameArr = []

    for path,dirlist,filelist in g:
        for filename in filelist:
            if filename[-4:] == "vmdk":
                filepath = os.path.join(path,filename)
                print("------------------------------------")
                print("current reading is " + filepath + "...")
                print("---------------read_vmdk_start----------------")
                vmdkInfoArr = getVMDKinfo(filepath)
                CurrentVMDK = vmdkInfoArr[0]
                CID = vmdkInfoArr[1]
                ParentVMDK = vmdkInfoArr[2]
                ParentCID = vmdkInfoArr[3]
                if CurrentVMDK not in nameArr:
                    nameArr.append(CurrentVMDK)
                    print(nameArr)
                    dot.node(CurrentVMDK,CurrentVMDK + " (CID: " + CID + ")")
                    if ParentVMDK not in nameArr:
                        nameArr.append(ParentVMDK)
                        print(nameArr)
                        dot.node(ParentVMDK,ParentVMDK + " (CID: " + ParentCID + ")")
                if ParentCID != "ffffffff":
                    dot.edge(ParentVMDK,CurrentVMDK,arrowhead='normal')

    # print(dot.source)
    dot.view()

if __name__ == "__main__":
    path = input("input VMDK file's Path:")
    print("current path is " + path)
    drawVMDKinfo(path)
