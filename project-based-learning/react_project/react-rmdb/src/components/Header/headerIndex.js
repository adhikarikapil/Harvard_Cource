import React from 'react';

// Logo images
import RMDBLogo from '../../images/react-movie-logo.svg'
import TMDBLogo from '../../images/tmdb_logo.svg'
// styles
import { Wrapper, Content, LogoImg, TMDBLogoImg } from './Header.styles';

const Header = () => (
    <Wrapper>
        <Content>
            <LogoImg src={RMDBLogo} alt='RMDB-logo'/>
            <TMDBLogoImg src={TMDBLogo} alt='TMDB-logo'/>
        </Content>
    </Wrapper>
);

export default Header;