import textwrap

parrafo = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras risus neque,
mollis a iaculis placerat, consectetur eget mauris. Phasellus pretium lorem velit, sit
amet scelerisque nulla egestas interdum. Nunc nec pellentesque orci, sit amet egestas
est. Aliquam erat volutpat. Pellentesque habitant morbi tristique senectus et netus et
malesuada fames ac turpis egestas. Sed tincidunt iaculis turpis eget feugiat. Curabitur
vehicula eu neque et aliquam.

Sed semper egestas felis, ac fringilla arcu bibendum sit amet. Nam vel pellentesque ante.
Duis id est id lorem egestas sollicitudin. Phasellus metus sem, dictum eu ipsum et,
congue gravida nulla. Suspendisse potenti. Sed eget diam bibendum, facilisis lectus
vestibulum, lacinia ligula. Cras eget tristique elit. Praesent eget sem purus. Quisque
sit amet metus non velit placerat mollis eget ac odio. Nulla hendrerit erat vitae sapien
auctor posuere. Aenean euismod lectus ipsum, gravida pretium est ultrices sed. Etiam
sodales dictum turpis in ornare. Suspendisse diam ante, aliquam eget diam vel, sollicitudin
placerat lacus. Vivamus sollicitudin urna mi, tempus gravida risus auctor ac. Morbi scelerisque,
libero nec rutrum tincidunt, ligula enim dignissim tellus, sodales vehicula erat ante a
nulla. Mauris sed eros eleifend nisl pulvinar gravida quis sed arcu.'''
long_linea = 60


def centrar_texto(parrafo, linea):
    parrafo = textwrap.wrap(parrafo)
    for i in parrafo:
        if (len(i) < 100):
            i = ' ' * (round(50 - len(i) / 2)) + i
            print(i)

centrar_texto(parrafo, long_linea)