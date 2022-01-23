def edit_dist(a, b, i, sum):
    if((i == -1) and (a.replace('*', '') == b.replace('*', ''))):
        print("in main")
        print(a)
        print(sum)
        return sum
    elif(i == -1):
        return 10**5
    else:
        # insert a
        # if(i == len(b) - 1):
        #     insert_a = a.join(b[i])
        # else:
        prei_a = a[:i+1]
        posti_a = a[i+1:]
        prei_a = prei_a + (b[i])
        insert_a = prei_a + (posti_a)

        # delete a
        # if(i == len(b) - 1):
        #     delete_a = a[:i]
        # else:
        pred_a = a[:i]
        postd_a = a[i+1:]
        delete_a = pred_a + (postd_a)
    # substitution
        pre_a = a[:i]
        post_a = a[i+1:]
        pre_a = pre_a + (b[i])
        sub_a = pre_a + (post_a)

        return min((edit_dist(insert_a, b, i - 1, sum + 1)),
                    (edit_dist(sub_a, b, i - 1, sum + 1)),
                    (edit_dist(delete_a, b, i - 1, sum + 1)),
                    (edit_dist(a, b, i - 1, sum)))


if(__name__ == '__main__'):
    print(edit_dist('junk*', 'clunky', len('clunky') - 1, 0))
