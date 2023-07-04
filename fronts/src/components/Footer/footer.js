import React from "react";
import {
	Box,
	Column,
	FooterLink,
	Row,
} from "./footerStyles";
import { Preview } from '@react-email/preview';
import FacebookOutlinedIcon from '@mui/icons-material/FacebookOutlined';
import InstagramIcon from '@mui/icons-material/Instagram';
import TwitterIcon from '@mui/icons-material/Twitter';


const Footer = () => {
	const email = 'buscalibro.cl@gmail.com';
	return (
		<Box>
			<h1 style={{
				color: "white",
				textAlign: "center",
			}}>
				BuscaLibro
			</h1>
			<Column>
				<FooterLink href={`mailto:${email}`}>Buscalibro@gmail.com</FooterLink>
				<FooterLink >Copyright © 2023 Todos los derechos reservados</FooterLink>
			</Column>
			<Row>
				<FacebookOutlinedIcon style={{ fontSize: "80px", color: "white" }} />
				<InstagramIcon style={{ fontSize: "80px", color: "white" }} />
				<TwitterIcon style={{ fontSize: "80px", color: "white" }} />

			</Row>

		</Box>
	);
};
export default Footer;
