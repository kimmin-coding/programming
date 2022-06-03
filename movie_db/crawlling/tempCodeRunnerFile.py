
answer=sorted(dic,key=lambda x:x[1])[0]

index=rgba.index(answer)
print(index)
btns[index].click()

print("done")