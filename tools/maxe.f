c converts binary file to ascii file
c
c   maxe.f
c
c       maximum eccentricities of each test particles.
c       output:
c       t_maximum, a_initial, e_maximum, id

	include 'swift.inc'

	real*8 xht(NTPMAX),yht(NTPMAX),zht(NTPMAX)
	real*8 vxht(NTPMAX),vyht(NTPMAX),vzht(NTPMAX)

	real*8 mass(NPLMAX),dr,peri,apo
	real*8 xh(NPLMAX),yh(NPLMAX),zh(NPLMAX)
	real*8 vxh(NPLMAX),vyh(NPLMAX),vzh(NPLMAX)

	integer istat(NTPMAX,NSTAT)
        real*8 rstat(NTPMAX,NSTATR)
	integer nbod,ntp,ierr,ifol,istep,count
	integer iflgchk,iu,nleft,i,id,idi(NTPMAX),ninit
        integer io_read_hdr,io_read_line
        integer io_read_hdr_r,io_read_line_r

	real*8 t0,tstop,dt,dtout,dtdump
	real*8 t,tmax
C   BG

	real*8 rmin,rmax,rmaxu,qmin,rplsq(NPLMAX),em(NTPMAX),ai(NTPMAX)
        logical*2 lclose
        real*8 a,e,inc,capom,omega,capm,j2rp2,j4rp4,te(NTPMAX)
        real*8 elh,elk,elp,elq

	character*80 outfile,inparfile,inplfile,intpfile,fopenstat

c Get data for the run and the test particles
C	write(*,*) 'Enter name of parameter data file : '
C	read(*,999) inparfile
        inparfile = 'dump_param.dat'
	call io_init_param(inparfile,t0,tstop,dt,dtout,dtdump,
     &         iflgchk,rmin,rmax,rmaxu,qmin,lclose,outfile,fopenstat)

c Prompt and read name of planet data file
	write(*,*) ' '
C	write(*,*) 'Enter name of planet data file : '
C	read(*,999) inplfile
999 	format(a)
        inplfile = 'dump_pl.dat'
	call io_init_pl(inplfile,lclose,iflgchk,nbod,mass,xh,yh,zh,
     &       vxh,vyh,vzh,rplsq,j2rp2,j4rp4)

c Get data for the run and the test particles
C	write(*,*) 'Enter name of test particle data file : '
C	read(*,999) intpfile
        intpfile = 'dump_tp.dat'
	call io_init_tp(intpfile,ntp,xht,yht,zht,vxht,vyht,
     &               vzht,istat,rstat)

        iu = 20
        em = 0
        ai = 0
        te = 0
        idi = 0
        count = 0
        dr = 180.0/PI

        if(btest(iflgchk,0)) then
           write(*,*) ' Reading an integer*2 binary file '
        else if(btest(iflgchk,1)) then
           write(*,*) ' Reading an real*4 binary file '
        else
           write(*,*) ' ERROR: no binary file format specified '
           write(*,*) '        in param file '
           stop
        endif

        open(unit=iu, file=outfile, status='old',form='unformatted')
        open(unit=7,file='maxe.out')

 1      continue
        tmax = t0
             if(btest(iflgchk,0))  then ! bit 0 is set
                ierr = io_read_hdr(iu,t,nbod,nleft)
             else
                ierr = io_read_hdr_r(iu,t,nbod,nleft)
             endif
             if(ierr.ne.0) goto 2

C   BG  Assume found            istep = 0
	     istep = 1
            do i=2,nbod
                if(btest(iflgchk,0))  then ! bit 0 is set
                   ierr = io_read_line(iu,id,a,e,inc,capom,omega,capm)
                else
                   ierr = io_read_line_r(iu,id,a,e,inc,capom,omega,capm)
                endif
                if(ierr.ne.0) goto 2
             enddo

             do i=1,nleft
                if(btest(iflgchk,0))  then ! bit 0 is set
                   ierr = io_read_line(iu,id,a,e,inc,capom,omega,capm)
                else
                   ierr = io_read_line_r(iu,id,a,e,inc,capom,omega,capm)
                endif
                if(ierr.ne.0) goto 2
                if(count.eq.0) then
                   ai(id) = a
                   idi(id) = id
                   ninit = nleft
                endif
                if(e.gt.em(i)) then
                   em(id) = e
                endif
                te(id)=t
             enddo
             count = count + 1
             if(istep.eq.0) goto 2     ! did not find particle this times step

        goto 1

 2      continue
        write(*,*) 'Start writing!'
        do i=1,ninit
            write(7,1002) te(i),ai(i),em(i),idi(i)
 1002   format(1x,e13.5,1x,f10.4,1x,f7.5,1x,i5)
        enddo
        write(*,*) 'DONE!'
        stop
        end
