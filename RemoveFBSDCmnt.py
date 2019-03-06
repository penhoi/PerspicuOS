import os,sys
import unittest

import unittest


def remove_comment_foreach_line(liLines, cTerminal, szCmnt):
    newflines = []
    for l in liLines:
        nidx = l.find(szCmnt)
        if nidx == -1:
            nl = l
        elif nidx >= 1:
            pre = l[:nidx]
            ridx = l.find(cTerminal, nidx)
            if ridx == -1:
                print(l)
            assert(ridx != -1)
            tail = l[ridx:]

            nl = pre + "FreeBSD" + tail
        else:
            nl = "\n"

        newflines.append(nl)
    #end for
    return newflines


def remove_comment(fname):
    # * $FreeBSD: release/9.0.0/sys/sys/acct.h 169857 2007-05-22 06:51:38Z dds $
    szCmnt = "FreeBSD: release/9.0.0"
    cliTerminal = "$"

    with open(fname, "r") as f:
        flines = f.readlines()

    newflines = remove_comment_foreach_line(flines, cTerminal, szCmnt)

    with open(fname, "w") as f:
        f.writelines(newflines)



def collect_files(root_dir):
    #fname = "/home/ws/project/PerspicuOS/FreeBSD9-orig/sys/sys/acct.h"
    #remove_comment(fname)

    # traverse root directory, and list directories as dirs and files as files
    for root, _dirs, files in os.walk(root_dir):
        for file in files:
            fname = os.path.join(root, file)
            remove_comment(fname)



"""
1. __FBSDID("$FreeBSD: release/9.0.0/bin/cat/cat.c 184471 2008-10-30 14:05:57Z ivoras $");
    ==> __FBSDID("$FreeBSD$");
2.  * $FreeBSD: release/9.0.0/sys/sys/apm.h 200557 2009-12-14 22:47:09Z rpaulo $
    ==>  * $FreeBSD$
3. echo '$FreeBSD: release/9.0.0/sys/boot/powerpc/boot1.chrp/generate-hfs.sh 183863 2008-10-14 03:32:41Z nwhitehorn $' >> $OUTPUT_FILE.bz2.uu
    ==> echo '$FreeBSD$' >> $OUTPUT_FILE.bz2.uu

more:
'.asciz "$FreeBSD: release/9.0.0/lib/libstand/i386/_setjmp.S 192760 2009-05-25 14 37 10Z attilio $"', 'lib/libstand/i386/_setjmp.S', =>
'.asciz "$FreeBSD$"'

'@c $FreeBSD: release/9.0.0/gnu/usr.bin/binutils/doc/asconfig.texi 218822 2011-02-18 20 54 12Z dim $', 'gnu/usr.bin/binutils/doc/asconfig.texi', =>
'@c $FreeBSD$'

'" * Created from $FreeBSD: release/9.0.0/sys/tools/vnode_if.awk 211616 2010-08-22 11 18 57Z rpaulo $\n" \', 'sys/tools/vnode_if.awk', =>
'" * Created from $FreeBSD$\n" \'

'%%CreationDate: $FreeBSD: release/9.0.0/share/doc/papers/timecounter/fig4.eps 116411 2003-06-15 18 49 46Z phk $', 'share/doc/papers/timecounter/fig4.eps', =>
'%%CreationDate: $FreeBSD$'

'#define RCSBASE "$FreeBSD: release/9.0.0/gnu/usr.bin/rcs/lib/rcsbase.h 50472 1999-08-27 23 37 10Z peter $"', 'gnu/usr.bin/rcs/lib/rcsbase.h', =>
'#define RCSBASE "$FreeBSD$"'

'__FBSDID("$FreeBSD: release/9.0.0/bin/pax/options.c 222177 2011-05-22 14 03 38Z uqs $");', 'bin/pax/options.c', =>
'__FBSDID("$FreeBSD$");'

'%__FBSDID("$FreeBSD: release/9.0.0/include/rpcsvc/bootparam_prot.x 114629 2003-05-04 02 51 42Z obrien $");', 'include/rpcsvc/bootparam_prot.x', =>
'%__FBSDID("$FreeBSD$");'

'# $FreeBSD: release/9.0.0/libexec/getty/Makefile 201380 2010-01-02 09 50 19Z ed $', 'libexec/getty/Makefile', =>
'# $FreeBSD$'

' * $FreeBSD: release/9.0.0/libexec/getty/pathnames.h 50476 1999-08-28 00 22 10Z peter $', 'libexec/getty/pathnames.h', =>
' * $FreeBSD$'

' "$FreeBSD: release/9.0.0/libexec/getty/subr.c 131091 2004-06-25 10 11 28Z phk $";', 'libexec/getty/subr.c', =>
' "$FreeBSD$";'

'.\" $FreeBSD: release/9.0.0/libexec/getty/ttys.5 202274 2010-01-14 05 35 32Z ed $', 'libexec/getty/ttys.5', =>
'.\" $FreeBSD$'

'libId(keepId, "$FreeBSD: release/9.0.0/gnu/usr.bin/rcs/lib/rcskeep.c 50472 1999-08-27 23 37 10Z peter $")', 'gnu/usr.bin/rcs/lib/rcskeep.c', =>
'libId(keepId, "$FreeBSD$")'

'mainProg(ciId, "ci", "$FreeBSD: release/9.0.0/gnu/usr.bin/rcs/ci/ci.c 50472 1999-08-27 23 37 10Z peter $")', 'gnu/usr.bin/rcs/ci/ci.c', =>
'mainProg(ciId, "ci", "$FreeBSD$")'

'__RCSID("$FreeBSD: release/9.0.0/sbin/routed/input.c 190745 2009-04-05 18 28 42Z phk $");', 'sbin/routed/input.c', =>
'__RCSID("$FreeBSD$");'

'SND_DECLARE_FILE("$FreeBSD: release/9.0.0/sys/dev/sound/isa/ad1816.c 193640 2009-06-07 19 12 08Z ariff $");', 'sys/dev/sound/isa/ad1816.c', =>
'SND_DECLARE_FILE("$FreeBSD$");'

'static char rcsid[] = "$FreeBSD: release/9.0.0/lib/libcompat/4.1/ftime.c 211061 2010-08-08 08 19 23Z ed $";', 'lib/libcompat/4.1/ftime.c', =>
'static char rcsid[] = "$FreeBSD$";'

'static const char rcsid[] = "@(#)$FreeBSD: release/9.0.0/sys/contrib/ipfilter/netinet/fil.c 196019 2009-08-01 19 26 27Z rwatson $";', 'sys/contrib/ipfilter/netinet/fil.c', =>
'static const char rcsid[] = "@(#)$FreeBSD$";'

'VERSIONID(`$FreeBSD: release/9.0.0/etc/sendmail/freebsd.mc 223068 2011-06-14 04 33 43Z gshapiro $')', 'etc/sendmail/freebsd.mc' =>
'VERSIONID(`$FreeBSD$')'

'#$FreeBSD: release/9.0.0/usr.sbin/pc-sysinstall/examples/pcinstall.cfg.zfs 209513 2010-06-24 22:21:47Z imp $', 'usr.sbin/pc-sysinstall/examples/pcinstall.cfg.zfs' =>
'#$FreeBSD$'

'%%$FreeBSD: release/9.0.0/games/fortune/datfiles/murphy-o 174425 2007-12-07 22:41:39Z dougb $', 'games/fortune/datfiles/murphy-o' =>
%%$FreeBSD$

"ident='$FreeBSD: release/9.0.0/tools/build/options/makeman 221733 2011-05-10 13:01:11Z ru $'", 'tools/build/options/makeman' =>
"ident='$FreeBSD$'"

"diff -I\$FreeBSD: release/9.0.0/tools/test/iconv/tablegen/cmp.sh 219019 2011-02-25 00:04:39Z gabor $1 $2 | grep '^-'", 'FreeBSD9-orig/tools/test/iconv/tablegen/cmp.sh' =>
"diff -I\$FreeBSD$1 $2 | grep '^-'"

"""

class TestAlgorithm(unittest.TestCase):
    def test_cases(self):
        mapCase = {
            '__FBSDID("$FreeBSD: release/9.0.0/bin/cat/cat.c $");' : '__FBSDID("$FreeBSD$");',
            '* $FreeBSD: release/9.0.0/sys/sys/apm.h $' : '* $FreeBSD$',
            'echo "$FreeBSD: release/9.0.0/sys/boot/powerpc/boot1.chrp/generate-hfs.sh $" >> $uu' : 'echo "$FreeBSD$" >> $uu',
            '.asciz "$FreeBSD: release/9.0.0/lib/libstand/i386/_setjmp.S $"' : '.asciz "$FreeBSD$"',
            '\@c $FreeBSD: release/9.0.0/gnu/usr.bin/binutils/doc/asconfig.texi $' : '\@c $FreeBSD$',
            '" * Created from $FreeBSD: release/9.0.0/sys/tools/vnode_if.awk $\n" \'' : '" * Created from $FreeBSD$\n" \'',
            'CreationDate: $FreeBSD: release/9.0.0/share/doc/papers/timecounter/fig4.eps $' : 'CreationDate: $FreeBSD$',
            '#define RCSBASE "$FreeBSD: release/9.0.0/gnu/usr.bin/rcs/lib/rcsbase.h $"' : '#define RCSBASE "$FreeBSD$"',
            '__FBSDID("$FreeBSD: release/9.0.0/bin/pax/options.c uqs $");' : '__FBSDID("$FreeBSD$");',
            '%__FBSDID("$FreeBSD: release/9.0.0/include/rpcsvc/bootparam_prot.x $");' : '%__FBSDID("$FreeBSD$");',
            '# $FreeBSD: release/9.0.0/libexec/getty/Makefile $' : '# $FreeBSD$',
            '* $FreeBSD: release/9.0.0/libexec/getty/pathnames.h $' : '* $FreeBSD$',
            '"$FreeBSD: release/9.0.0/libexec/getty/subr.c $";' : '"$FreeBSD$";',
            '.\" $FreeBSD: release/9.0.0/libexec/getty/ttys.5 $' : '.\" $FreeBSD$',
            'libId(keepId, "$FreeBSD: release/9.0.0/gnu/usr.bin/rcs/lib/rcskeep.c $")' : 'libId(keepId, "$FreeBSD$")',
            'mainProg(ciId, "ci", "$FreeBSD: release/9.0.0/gnu/usr.bin/rcs/ci/ci.c $")' : 'mainProg(ciId, "ci", "$FreeBSD$")',
            '__RCSID("$FreeBSD: release/9.0.0/sbin/routed/input.c $");' : '__RCSID("$FreeBSD$");',
            'SND_DECLARE_FILE("$FreeBSD: release/9.0.0/sys/dev/sound/isa/ad1816.c $");' : 'SND_DECLARE_FILE("$FreeBSD$");',
            'static char rcsid[] = "$FreeBSD: release/9.0.0/lib/libcompat/4.1/ftime.c $";' : 'static char rcsid[] = "$FreeBSD$";',
            'static const char rcsid[] = "@(#)$FreeBSD: release/9.0.0/sys/contrib/ipfilter/netinet/fil.c $";' : 'static const char rcsid[] = "@(#)$FreeBSD$";',
            'VERSIONID(`$FreeBSD: release/9.0.0/etc/sendmail/freebsd.mc $\')' : 'VERSIONID(`$FreeBSD$\')',
            '#$FreeBSD: release/9.0.0/usr.sbin/pc-sysinstall/examples/pcinstall.cfg.zfs $' : '#$FreeBSD$',
            '%%$FreeBSD: release/9.0.0/games/fortune/datfiles/murphy-o 174425 2007-12-07 22:41:39Z dougb $' : '%%$FreeBSD$',
            "ident='$FreeBSD: release/9.0.0/tools/build/options/makeman 221733 2011-05-10 13:01:11Z ru $'" : "ident='$FreeBSD$'",
            "diff -I\\$FreeBSD: release/9.0.0/tools/test/iconv/tablegen/cmp.sh $1 $2 | grep '^-'" : "diff -I\\$FreeBSD$1 $2 | grep '^-'"
        }

        szCmnt = "FreeBSD: release/9.0.0"
        cTerminal = "$"
        liLines = list(mapCase.keys())

        liRet = remove_comment_foreach_line(liLines, cTerminal, szCmnt)
        liExpect = list(mapCase.values())

        self.assertEqual(liRet, liExpect)



if __name__ == "__main__":
    if len(sys.argv) == 1:
        unittest.main()
        exit(0)

    elif len(sys.argv) > 2:
        print("Usage:\n\t%s root_directory" % (sys.argv[0]))
        exit(-1)

    collect_files(sys.argv[1])
