from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# bresenham line drawing algorithm
def bresenham(x1, y1, x2, y2):
    # 10,30,90,70
    # m = (y2 - y2) / (x2 - x2) 
    # m = (70 - 30) / (90 - 10) = .5

    dx = x2 - x1
    dy = y2 - y1
    # d1 = 2*dy
    # d2 = 2*(dx-dy)
    # p = d1 - dx
    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1
    dx = abs(dx)
    dy = abs(dy)
    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0
    D = 2*dy - dx
    y = 0
    for x in range(dx+1): 
        # menggambar titik pada koordinat x dan y dengan nilai satuan berupa integer
        glVertex2i(x1 + x*xx + y*yx, y1 + x*xy + y*yy)

        if D > 0:
            y += 1
            D -= 2*dx
        D += 2*dy

def display():
    # Membersihkan window
    glClear(GL_COLOR_BUFFER_BIT)
    # Menentukan Warna
    glColor3f(0.0, 1.0, 0.0)
    # Spesifikasikan diameter dari pixel yang akan digammbar
    glPointSize(5.0)
    # Memilih mode point
    glBegin(GL_POINTS)
    # Membuat titik
    bresenham(10,30,90,70)
    glEnd()
    glFlush()

def main():
    # Inisialisasi glut
    glutInit(sys.argv)
    # Inisialisasi tipe display glut
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    # Inisialisasi ukuran layar
    glutInitWindowSize(1000, 1000)
    # Inisialisasi posisi window
    glutInitWindowPosition(25, 25)
    # inisialisasi pembuatan window
    glutCreateWindow(b"Bresenham's line algorithm")
    # Membersihkan layar dan memberikan warna background
    glClearColor(0.0, 0.0, 0.0, 0.0)
    # Set origin dari grid dan ukurannya 75 x 75
    gluOrtho2D(0, 75, 0, 75)
    # Memanggil fungsi display
    glutDisplayFunc(display)
    glutMainLoop()

main()