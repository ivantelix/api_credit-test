
import Page from 'material-ui-shell/lib/containers/Page'
import React, { useState, Fragment } from 'react'
import { useIntl } from 'react-intl'
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Stepper from '@material-ui/core/Stepper';
import Step from '@material-ui/core/Step';
import StepLabel from '@material-ui/core/StepLabel';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';
import TextField from '@material-ui/core/TextField';
import axios from 'axios';

const useStyles = makeStyles((theme) => ({
  appBar: {
    position: 'relative',
  },
  layout: {
    width: 'auto',
    marginLeft: theme.spacing(2),
    marginRight: theme.spacing(2),
    [theme.breakpoints.up(600 + theme.spacing(2) * 2)]: {
      width: 600,
      marginLeft: 'auto',
      marginRight: 'auto',
    },
  },
  paper: {
    marginTop: theme.spacing(3),
    marginBottom: theme.spacing(3),
    padding: theme.spacing(2),
    [theme.breakpoints.up(600 + theme.spacing(3) * 2)]: {
      marginTop: theme.spacing(6),
      marginBottom: theme.spacing(6),
      padding: theme.spacing(3),
    },
  },
  stepper: {
    padding: theme.spacing(3, 0, 5),
  },
  buttons: {
    display: 'flex',
    justifyContent: 'flex-end',
  },
  button: {
    marginTop: theme.spacing(3),
    marginLeft: theme.spacing(1),
  },
}));

const steps = ['Datos de Solicitud'];

const FormCredit = () => {
  const classes = useStyles();
  const [activeStep, setActiveStep] = useState(0);
  const [datos, setDatos] = useState({
    name: "",
    lastname: "",
    dni: null,
    credit_amount: null,
    comment: ""

  });

  const handleInputChange = (e) => {
  setDatos({
    ...datos,
    [e.target.name]: e.target.value,
  })
}

  const handleNext = () => {
    setActiveStep(activeStep + 1);

    const config = {
        headers: { 'content-type': 'multipart/form-data' }
    }

    axios.post('localhost:8000/credit/create/', datos, config)
      .then((response) => {
        console.log('exito')
      })
      .catch((err) => {
          console.error('No hemos podido generar su solicitud.');
      });              


    
    console.log(datos)
  };

  const handleBack = () => {
    setActiveStep(activeStep - 1);
  };
  const intl = useIntl()

  return (
    <Page
      pageTitle={intl.formatMessage({
        id: 'credit-request',
        defaultMessage: 'Solicitud de Credito',
      })}
    >
      <Fragment>
        <main className={classes.layout}>
          <Paper className={classes.paper}>
            <Typography component="h1" variant="h4" align="center">
              Solicitud de Credito
            </Typography>
            <Stepper activeStep={activeStep} className={classes.stepper}>
              {steps.map((label) => (
                <Step key={label}>
                  <StepLabel>{label}</StepLabel>
                </Step>
              ))}
            </Stepper>
            <Fragment>
              {activeStep === steps.length ? (
                <Fragment>
                  <Typography variant="h5" gutterBottom>
                    Solicitud de credito realizada!
                  </Typography>
                  <Typography variant="subtitle1">
                    Hemos enviado la confirmación de su solicitud a un administrador.
                  </Typography>
                </Fragment>
              ) : (
                <Fragment>
                    {
                        <Grid container spacing={3}>
                          <Grid item xs={12} sm={6}>
                            <TextField
                              required
                              id="name"
                              name="name"
                              label="Nombres"
                              onChange={handleInputChange}
                              fullWidth
                              autoComplete="given-name"
                            />
                          </Grid>
                          <Grid item xs={12} sm={6}>
                            <TextField
                              required
                              id="lastName"
                              name="lastname"
                              label="Apellidos"
                              onChange={handleInputChange}
                              fullWidth
                              autoComplete="family-name"
                            />
                          </Grid>
                          <Grid item xs={12} sm={6}>
                            <TextField
                              required
                              id="dni"
                              name="dni"
                              label="DNI"
                              onChange={handleInputChange}
                              fullWidth
                              autoComplete="shipping address-level2"
                            />
                          </Grid>
                          <Grid item xs={12} sm={6}>
                            <TextField
                              required
                              id="credit_amount"
                              name="credit_amount"
                              label="Monto de credito"
                              onChange={handleInputChange}
                              fullWidth
                              autoComplete="shipping postal-code"
                            />
                          </Grid>
                          <Grid item xs={12}>
                            <TextField
                              id="comment"
                              name="comment"
                              label="Comentario"
                              onChange={handleInputChange}
                              fullWidth
                            />
                          </Grid>
                        </Grid>
                  }
                  <div className={classes.buttons}>
                    {activeStep !== 0 && (
                      <Button onClick={handleBack} className={classes.button}>
                        Atras
                      </Button>
                    )}
                    <Button
                      variant="contained"
                      color="primary"
                      onClick={handleNext}
                      className={classes.button}
                    >
                      {activeStep === steps.length - 1 ? 'Solicitar' : 'Siguiente'}
                    </Button>
                  </div>
                </Fragment>
              )}
            </Fragment>
          </Paper>
        </main>
      </Fragment>
    </Page>
  )
}
export default FormCredit