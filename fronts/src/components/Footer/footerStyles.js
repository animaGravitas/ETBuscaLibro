import styled from 'styled-components';

export const Box = styled.div`
background: #3f51b5;
bottom: 0;
width: 100%;
display: flex;
flex-direction: column;
min-height: 48vh;

@media (max-width: 1000px) {
	padding: 70px 30px;
}
`;

export const Column = styled.div`
display: flex;
flex-direction: column;
text-align: center;
`;
export const Row = styled.div`
display: flex;
flex-direction: row;
justify-content: center;
gap: 77px;
`;


export const FooterLink = styled.a`
color: #fff;
margin-bottom: 20px;
font-size: 18px;
text-decoration: none;

&:hover {
	color: black;
	transition: 200ms ease-in;
}
`;

export const FacebookOutlinedIcon = styled.div`
&:hover {
	color: black;
	// transition: 200ms ease-in;
}
`;