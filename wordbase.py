import re;
import os;

def findwords(startswith):
    f = open(dict_path,'r');
    wlist = f.read();
    #wlist = wlist.lower();

    pattern = "\s" + startswith + "[a-z]*" + "\s";

    words = re.findall(pattern,wlist);

    for i in range(len(words)):
        words[i] = words[i].strip();

    #print words;
    return words;


def neighbors(width, height, x,y,grid):
    neigh = [];
    seq1 = (1,0,-1);
    offsets = [(m,n) for m in seq1 for n in seq1];
    offsets.remove((0,0));
    pos = []
    for off in offsets:
        xp = x + off[0];
        yp = y + off[1];
        
        if (xp < width) and (xp > -1) and (yp < height) and (yp > -1):
            #print str(xp) + " " + str(yp);
            neigh.append(grid[yp][xp]);
            pos.append((xp,yp));
        
    return [neigh,pos];

def find_words(x,y,possible_words,visited):
    rem_words = [];
    #print "find words x:" + str(x) + " y: " + str(y);
    
    #append all words that end in (x,y) to global list
    for w in possible_words:
        if (len(w) <= len(visited)+1):
            #print w;
            rem_words.append(w);
            word_list.append(w);

    #remove all words that end in (x,y) from the remove words list
    for w in rem_words:
        possible_words.remove(w);

    #return a list of neighbouring characters and grid positions from (x,y)
    [neigh,pos] = neighbors(10,13,x,y,grid);

    #print possible_words;
    #check neighbouring positions for longer words
    #print len(neigh);
    #print visited;
    for k in range(len(neigh)):
        if not(pos[k] in visited):
            pw = [];        #new list of possible words
            for w in possible_words:
                if (w[len(visited)+1] == neigh[k]):
                    pw.append(w);
            if (pw):
                nv = visited[:];
                nv.append((x,y));
                find_words(pos[k][0],pos[k][1],pw,nv);

            
def f_words(sx,sy):
    [neigh,pos] = neighbors(width,height,sx,sy,grid);
    for i in range(len(neigh)):
        start_str = grid[sy][sx] + neigh[i];
        pw = findwords(start_str);
        if (pw):
            find_words(pos[i][0],pos[i][1],pw,[(sx,sy)]);
    


word_list = [];
width = 10;
height = 13;

grid = [['a' for x in xrange(width)] for x in xrange(height)];

#file names
grid_path = "wbase_grid.txt";
dict_path = "wordlist.txt";

#read in the word base grid
fgrid = open(grid_path,"r");
n = 0;
for line in fgrid:
    l = line.split(' ');
    for i in range(10):
        grid[n][i] = l[i].strip();
    n=n+1;
fgrid.close();

#2D list array to hold the results
results = [[[]for x in xrange(width)] for x in xrange(height)];


user_in = '';
print ("Enter the x,y position you want to find words for. 0,0 is top left corner");

while(user_in != 'q'):
    user_in = raw_input('x,y: ');
    if (user_in.strip() != 'q'):
        p = user_in.split(',');
        px = int(p[0].strip());
        py = int(p[1].strip());
        word_list = [];
        if (px < width) and (py < height):
            f_words(px,py);
            print(word_list);
            
    








        

