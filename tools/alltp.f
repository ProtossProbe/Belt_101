c converts binary file to ascii file
c
c   alltp.f
c
c       outputs elements of all test particles at any time wanted.

	include 'swift.inc'

	real*8 xht(NTPMAX),yht(NTPMAX),zht(NTPMAX)
	real*8 vxht(NTPMAX),vyht(NTPMAX),vzht(NTPMAX)

	real*8 mass(NPLMAX),dr,peri,apo
	real*8 xh(NPLMAX),yh(NPLMAX),zh(NPLMAX)
	real*8 vxh(NPLMAX),vyh(NPLMAX),vzh(NPLMAX)

	integer istat(NTPMAX,NSTAT)
        real*8 rstat(NTPMAX,NSTATR)
	integer nbod,ntp,ierr,ifol,istep
	integer iflgchk,iu,nleft,i,id
        integer io_read_hdr,io_read_line
        integer io_read_hdr_r,io_read_line_r

	real*8 t0,tstop,dt,dtout,dtdump
	real*8 t,tmax
C   BG
	real*8 twant

	real*8 rmin,rmax,rmaxu,qmin,rplsq(NPLMAX)
        logical*2 lclose
        real*8 a,e,inc,capom,omega,capm,j2rp2,j4rp4
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

C   BG  write(*,*) ' Input the particle number to follow '
C   BG  read(*,*) ifol
C   BG  write(*,*) ' Following particle ',ifol

C   BG  the particle number should never be found!!
	ifol = -999

C   BG  get desired time.
	write(*,*) ' '
        write(*,*) ' Produce elements for all t.p. at what time?'
        read(*,*) twant
        write(*,*) ' Searching for t > ',twant

        open(unit=iu, file=outfile, status='old',form='unformatted')
        open(unit=7,file='alltp.out')
CCCCC        open(unit=8,file='alltp_hkpq.out')

        tmax = t0
 1      continue
             if(btest(iflgchk,0))  then ! bit 0 is set
                ierr = io_read_hdr(iu,t,nbod,nleft) 
             else
                ierr = io_read_hdr_r(iu,t,nbod,nleft) 
             endif

             if(ierr.ne.0) goto 2
             write(77,*) t,nbod,nleft

C   BG  Assume found            istep = 0
	     istep = 1
             do i=2,nbod
                if(btest(iflgchk,0))  then ! bit 0 is set
                   ierr = io_read_line(iu,id,a,e,inc,capom,omega,capm) 
                else
                   ierr = io_read_line_r(iu,id,a,e,inc,capom,omega,capm) 
                endif
                if(ierr.ne.0) goto 2
C   BG   The following conditional should never be true !
                if(id.eq.ifol) then
                   istep = 1
                   elh = e*cos(omega+capom)
                   elk = e*sin(omega+capom)
                   elp = sin(inc/2.0)*cos(capom)
                   elq = sin(inc/2.0)*sin(capom)
                   inc = inc*dr
                   capom = capom*dr
                   omega = omega*dr
                   capm = capm*dr
                   peri = a*(1.0d0-e)
                   write(7,1000) t,a,e,inc,capom,omega,capm,peri
 1000              format(1x,e13.5,1x,f10.4,1x,f7.5,4(1x,f9.4),1x,f10.4)
CCCCC                   write(8,1001) t,elh,elk,elp,elq
 1001              format(1x,e13.5,4(1x,f7.5))
                   tmax = t
                endif
             enddo

             do i=1,nleft
                if(btest(iflgchk,0))  then ! bit 0 is set
                   ierr = io_read_line(iu,id,a,e,inc,capom,omega,capm) 
                else
                   ierr = io_read_line_r(iu,id,a,e,inc,capom,omega,capm) 
                endif
                if(ierr.ne.0) goto 2
C   BG                if(id.eq.ifol) then
                if(t .gt. twant) then
C   BG                   istep = 1
                   istep = 0			! causes exit
C                    elh = e*cos(omega+capom)
C                    elk = e*sin(omega+capom)
C                    elp = sin(inc/2.0)*cos(capom)
C                    elq = sin(inc/2.0)*sin(capom)
                   inc = inc*dr
                   capom = capom*dr
                   omega = omega*dr
                   capm = capm*dr
                   peri = a*(1.0d0-e)
                   apo = a*(1.0d0+e)
CCC                   write(7,1002) t,a,e,inc,capom,omega,capm,peri,id
                   write(7,1002) t,a,e,inc,capom,omega,capm,apo,id
 1002    format(1x,e13.5,1x,f10.4,1x,f7.5,4(1x,f9.4),1x,f10.4,1x,i5)
                   tmax = t
CCC                   write(8,1001) t,elh,elk,elp,elq
                endif
             enddo
             if(istep.eq.0) goto 2     ! did not find particle this times step

        goto 1

 2      continue

        write(*,*) ' twant = ',twant, '       found time = ', t

        stop
        end
